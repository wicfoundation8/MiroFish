from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

def seed_db():
    db = SessionLocal()

    if db.query(models.Agent).first():
        print("Database already seeded.")
        db.close()
        return

    print("Seeding database with mock agents...")
    agents = [
        models.Agent(
            name="Quantum Arbitrage V2",
            description="High-frequency trading agent specialized in cross-DEX arbitrage on EVM chains. Uses advanced statistical models.",
            price=500.0,
            apy=125.4,
            win_rate=82.5,
            total_trades=14520,
            category="Crypto",
            author="0xQuant"
        ),
        models.Agent(
            name="Trend Catcher AI",
            description="Momentum trading bot that identifies and rides long-term trends in top 20 cryptocurrencies.",
            price=250.0,
            apy=65.2,
            win_rate=60.1,
            total_trades=340,
            category="Crypto",
            author="WicchainLabs"
        ),
        models.Agent(
            name="Stable Yield Farmer",
            description="Low-risk strategy that dynamically reallocates stablecoins across different DeFi lending protocols for optimal yield.",
            price=100.0,
            apy=15.8,
            win_rate=99.9,
            total_trades=5210,
            category="DeFi",
            author="DeFiGuru"
        ),
        models.Agent(
            name="Sentiment Sniper",
            description="NLP-based agent that trades based on Twitter and news sentiment analysis for specific altcoins.",
            price=750.0,
            apy=210.5,
            win_rate=55.4,
            total_trades=890,
            category="Crypto",
            author="NLP_Trader"
        )
    ]

    db.add_all(agents)
    db.commit()
    print("Database seeded successfully.")
    db.close()

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    seed_db()
