from sqlmodel import Field, SQLModel, create_engine, Relationship # type: ignore
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class Subscription(SQLModel, table= True):
    id: int= Field(primary_key= True)
    empresa: str
    site: Optional[str] = None
    data_assinatura:  date
    preco: Decimal

class Payments(SQLModel, table= True):
    id: int= Field(primary_key= True)
    subscription_id: int = Field(foreign_key= 'subscription.id')
    subscription: Subscription= Relationship()
    date: date
