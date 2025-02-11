from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

class BuyInBase(BaseModel):
    name: str
    buy_in_price: float
    cash_out_price: float
    winnings_losings_price: float

class BuyInModel(BuyInBase):
    id: int
    class Config:
        orm_mode = True
        
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post('/buy_ins/', response_model=BuyInModel)
async def create_buy_in(buy_in: BuyInBase, db: db_dependency):
    db_buy_in = models.BuyIn(name=buy_in.name, buy_in_price=buy_in.buy_in_price, cash_out_price=buy_in.cash_out_price, winnings_losings_price=buy_in.winnings_losings_price)
    db.add(db_buy_in)
    db.commit()
    db.refresh(db_buy_in)
    return db_buy_in

@app.get('/buy_ins/', response_model=List[BuyInModel])
async def read_buy_ins(db: db_dependency, skip: int = 0, limit: int = 100):
    buy_ins = db.query(models.BuyIn).offset(skip).limit(limit).all()
    return buy_ins
