from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class BuyIn(Base):
    __tablename__ = "buy_in"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    buy_in_price = Column(Float)
    cash_out_price = Column(Float)
    winnings_losings_price = Column(Float)