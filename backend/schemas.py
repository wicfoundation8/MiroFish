from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Agent Schemas
class AgentBase(BaseModel):
    name: str
    description: str
    price: float
    apy: float
    win_rate: float
    total_trades: int
    category: str
    author: str

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int

    class Config:
        from_attributes = True

# User Schemas
class UserBase(BaseModel):
    wallet_address: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    balance: float

    class Config:
        from_attributes = True

# Transaction Schemas
class TransactionBase(BaseModel):
    agent_id: int
    amount: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# Login Request
class LoginRequest(BaseModel):
    wallet_address: str

class BuyRequest(BaseModel):
    wallet_address: str
    agent_id: int
