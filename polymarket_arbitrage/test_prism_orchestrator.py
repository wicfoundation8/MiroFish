import asyncio
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from polymarket_arbitrage.prism_orchestrator import (
    PrismOrchestrator,
    HMMPredictor,
    SentimentAnalyst,
    WebSocketOrderFlowClient
)

@pytest.fixture
def mock_components():
    hmm_predictor = MagicMock(spec=HMMPredictor)
    hmm_predictor.predict = AsyncMock(return_value={"signal": "buy", "confidence": 0.8})

    sentiment_analyst = MagicMock(spec=SentimentAnalyst)
    sentiment_analyst.analyze = AsyncMock(return_value={"sentiment": "positive", "score": 0.9})

    ws_client = MagicMock(spec=WebSocketOrderFlowClient)
    ws_client.connect = AsyncMock()
    ws_client.disconnect = AsyncMock()
    ws_client.get_latest_order_flow = AsyncMock(return_value={"bids": [100], "asks": [101]})

    return hmm_predictor, sentiment_analyst, ws_client

@pytest.fixture
def orchestrator(mock_components):
    hmm, sentiment, ws = mock_components
    return PrismOrchestrator(hmm_predictor=hmm, sentiment_analyst=sentiment, ws_client=ws)

def test_initialization(orchestrator, mock_components):
    hmm, sentiment, ws = mock_components
    assert orchestrator.hmm_predictor == hmm
    assert orchestrator.sentiment_analyst == sentiment
    assert orchestrator.ws_client == ws
    assert orchestrator.is_running == False

def test_initialization_defaults():
    orch = PrismOrchestrator()
    assert isinstance(orch.hmm_predictor, HMMPredictor)
    assert isinstance(orch.sentiment_analyst, SentimentAnalyst)
    assert isinstance(orch.ws_client, WebSocketOrderFlowClient)

@pytest.mark.asyncio
async def test_run_loop(orchestrator, mock_components):
    hmm, sentiment, ws = mock_components

    # We need to run the loop but break out of it quickly.
    # A common way is to run it as a task, let it yield, then cancel it.
    task = asyncio.create_task(orchestrator.run())

    # Wait for the first iteration to likely finish
    await asyncio.sleep(0.1)

    # Check if things were called
    ws.connect.assert_called_once()
    assert ws.get_latest_order_flow.called
    assert hmm.predict.called
    assert sentiment.analyze.called

    assert orchestrator.is_running == True

    # Cancel it
    task.cancel()

    # Wait for cancellation to settle
    try:
        await task
    except asyncio.CancelledError:
        pass

    ws.disconnect.assert_called_once()
    assert orchestrator.is_running == False

def test_kill_switch(orchestrator):
    orchestrator.is_running = True
    orchestrator.kill_switch()
    assert orchestrator.is_running == False

@pytest.mark.asyncio
async def test_kill_switch_during_run(orchestrator, mock_components):
    hmm, sentiment, ws = mock_components

    # Override sleep to trigger kill_switch, ending the loop gracefully
    async def mock_sleep(*args, **kwargs):
        orchestrator.kill_switch()

    with patch("asyncio.sleep", new=mock_sleep):
        await orchestrator.run()

    # The loop should have run exactly once, then stopped
    ws.connect.assert_called_once()
    assert ws.get_latest_order_flow.called
    assert hmm.predict.called
    assert sentiment.analyze.called
    ws.disconnect.assert_called_once()
    assert orchestrator.is_running == False
