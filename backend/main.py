from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="WICAI4trade.AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/agents", response_model=List[schemas.Agent])
def read_agents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agents = db.query(models.Agent).offset(skip).limit(limit).all()
    return agents

@app.get("/agents/{agent_id}", response_model=schemas.Agent)
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@app.post("/users/login", response_model=schemas.User)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.wallet_address == request.wallet_address).first()
    if not user:
        user = models.User(wallet_address=request.wallet_address)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

@app.post("/marketplace/buy", response_model=schemas.Transaction)
def buy_agent(request: schemas.BuyRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.wallet_address == request.wallet_address).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    agent = db.query(models.Agent).filter(models.Agent.id == request.agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    if user.balance < agent.price:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Deduct balance
    user.balance -= agent.price

    # Create transaction
    transaction = models.Transaction(
        user_id=user.id,
        agent_id=agent.id,
        amount=agent.price
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction
