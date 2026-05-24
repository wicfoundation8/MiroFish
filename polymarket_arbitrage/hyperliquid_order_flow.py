import asyncio
import json
import logging
import time
import websockets
from typing import Dict, Any, Callable

logger = logging.getLogger("WicClawAI_Hyperliquid_OrderFlow")

class HyperliquidOrderFlowClient:
    """
    WebSocket Order Flow Client optimized for high-speed order flow logic
    on Hyperliquid, integrated with HMM regime signals.
    """
    def __init__(self, hmm_regime_model=None):
        self.ws_url = "wss://api.hyperliquid.xyz/ws"
        self.hmm_model = hmm_regime_model
        self.current_regime = "neutral"
        self.callbacks = []
        self._is_running = False
        self.latency_stats = []

    def register_callback(self, callback: Callable[[Dict[str, Any], str], None]):
        """Register a callback for high-speed order execution."""
        self.callbacks.append(callback)

    def _update_regime(self, market_data):
        """Update HMM regime based on incoming market data."""
        if self.hmm_model:
            # High-speed regime inference
            self.current_regime = self.hmm_model.predict_regime(market_data)

    async def process_order_flow(self, data: Dict[str, Any], receive_time: float):
        """Optimize high-speed order flow logic."""
        # 1. High-speed parsing - avoid slow key lookups if possible
        if data.get("channel") != "l2Book" or "data" not in data:
            return

        book_data = data["data"]

        # 2. Update HMM Regime signals
        self._update_regime(book_data)

        # 3. Execution readiness based on HMM regime
        # Fast path dispatch
        for callback in self.callbacks:
            asyncio.create_task(self._safe_callback(callback, book_data, self.current_regime))

        # Log latency
        process_time = time.time()
        self.latency_stats.append(process_time - receive_time)
        if len(self.latency_stats) > 1000:
            self.latency_stats = self.latency_stats[-1000:]

    async def _safe_callback(self, callback, data, regime):
        try:
            if asyncio.iscoroutinefunction(callback):
                await callback(data, regime)
            else:
                callback(data, regime)
        except Exception as e:
            logger.error(f"Error in order flow callback: {e}")

    async def connect_and_listen(self, coins=["BTC"]):
        """Establish WebSocket connection to Hyperliquid."""
        self._is_running = True

        try:
            # Use websockets optimization for higher throughput
            async with websockets.connect(
                self.ws_url,
                max_size=None,
                ping_interval=20,
                ping_timeout=20
            ) as websocket:
                logger.info(f"Connected to Hyperliquid Order Flow at {self.ws_url}")

                # Subscribe to order flow for each coin
                for coin in coins:
                    subscribe_msg = {
                        "method": "subscribe",
                        "subscription": {"type": "l2Book", "coin": coin}
                    }
                    await websocket.send(json.dumps(subscribe_msg))
                    logger.info(f"Subscribed to L2 book for {coin}")

                # High-speed listening loop
                while self._is_running:
                    try:
                        response = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                        receive_time = time.time()

                        # Use fast JSON decoding
                        data = json.loads(response)

                        # Process on event loop without blocking the receiver
                        asyncio.create_task(self.process_order_flow(data, receive_time))
                    except asyncio.TimeoutError:
                        # Keep alive heartbeat handling
                        pass
        except Exception as e:
            logger.error(f"Hyperliquid WebSocket connection error: {e}")

    def get_avg_latency(self):
        """Returns average processing latency in milliseconds."""
        if not self.latency_stats:
            return 0
        return (sum(self.latency_stats) / len(self.latency_stats)) * 1000

    def stop(self):
        self._is_running = False
