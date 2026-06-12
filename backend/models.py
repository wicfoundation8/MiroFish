from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
import datetime

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, unique=True, index=True)
    balance = Column(Float, default=10000.0) # Mock balance

    transactions = relationship("Transaction", back_populates="user")

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    apy = Column(Float) # Mock Annual Percentage Yield
    win_rate = Column(Float) # Mock win rate
    total_trades = Column(Integer, default=0)
    category = Column(String) # e.g., Crypto, Forex, Equities
    author = Column(String)

    transactions = relationship("Transaction", back_populates="agent")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    agent_id = Column(Integer, ForeignKey("agents.id"))
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    agent = relationship("Agent", back_populates="transactions")
