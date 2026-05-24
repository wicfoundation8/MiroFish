import pytest
from polymarket_arbitrage.sentiment_analyst import SentimentAnalyst

def test_track_hype_whale_movements():
    analyst = SentimentAnalyst()
    on_chain_data = [
        {'amount': 2000000, 'token': 'HYPE'},
        {'amount': 500000, 'token': 'HYPE'},
        {'amount': 1500000, 'token': 'OTHER'},
    ]
    social_data = [
        {'content': 'HYPE is going to the moon', 'is_whale': True},
        {'content': 'I like hype', 'is_whale': False},
        {'content': 'Another post', 'is_whale': True},
    ]

    result = analyst.track_hype_whale_movements(on_chain_data, social_data)

    assert result['hype_whale_count'] == 1
    assert result['hype_social_whale_mentions'] == 1
    assert result['signal_strength'] == 3

def test_track_skyai_rotation_signals():
    analyst = SentimentAnalyst()
    on_chain_data = [
        {'to_token': 'SKYAI', 'from_token': 'USDC'},
        {'from_token': 'SKYAI', 'to_token': 'ETH'},
        {'to_token': 'OTHER', 'from_token': 'USDC'},
    ]
    social_data = [
        {'content': 'SKYAI looks promising', 'sentiment_score': 10},
        {'content': 'Selling my skyai', 'sentiment_score': -5},
        {'content': 'No mention of token here', 'sentiment_score': 5},
    ]

    result = analyst.track_skyai_rotation_signals(on_chain_data, social_data)

    assert result['skyai_rotation_txs'] == 2
    assert result['skyai_social_sentiment'] == 5
    assert result['rotation_probability'] == 0.07

def test_track_skyai_rotation_signals_bounds():
    analyst = SentimentAnalyst()

    # Upper bound
    result_upper = analyst.track_skyai_rotation_signals([], [{'content': 'SKYAI', 'sentiment_score': 200}])
    assert result_upper['rotation_probability'] == 1.0

    # Lower bound
    result_lower = analyst.track_skyai_rotation_signals([], [{'content': 'SKYAI', 'sentiment_score': -50}])
    assert result_lower['rotation_probability'] == 0.0
