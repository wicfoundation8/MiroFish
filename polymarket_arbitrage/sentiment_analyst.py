from typing import Dict, Any, List

class SentimentAnalyst:
    """
    Skill node for analyzing sentiment and tracking movements.
    """
    def __init__(self):
        pass

    def track_hype_whale_movements(self, on_chain_data: List[Dict[str, Any]], social_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Track HYPE whale movements using on-chain and social data patterns.
        """
        whale_count = sum(1 for tx in on_chain_data if tx.get('amount', 0) > 1000000 and tx.get('token') == 'HYPE')
        social_mentions = sum(1 for post in social_data if 'HYPE' in post.get('content', '').upper() and post.get('is_whale', False))

        return {
            'hype_whale_count': whale_count,
            'hype_social_whale_mentions': social_mentions,
            'signal_strength': (whale_count * 2) + social_mentions
        }

    def track_skyai_rotation_signals(self, on_chain_data: List[Dict[str, Any]], social_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Track SKYAI rotation signals using on-chain and social data patterns.
        """
        rotation_txs = sum(1 for tx in on_chain_data if tx.get('to_token') == 'SKYAI' or tx.get('from_token') == 'SKYAI')
        social_sentiment = sum(post.get('sentiment_score', 0) for post in social_data if 'SKYAI' in post.get('content', '').upper())

        return {
            'skyai_rotation_txs': rotation_txs,
            'skyai_social_sentiment': social_sentiment,
            'rotation_probability': min(1.0, max(0.0, (rotation_txs + social_sentiment) / 100.0))
        }
