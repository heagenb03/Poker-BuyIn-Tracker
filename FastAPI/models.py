from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class BuyIn(Base):
    __tablename__ = 'buyins'

    id = Column(Integer, primary_key=True, index=True)
    player = Column(String)
    amount = Column(Float)
    is_active = Column(Boolean, default=True)
    