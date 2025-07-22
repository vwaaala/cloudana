# stake.py
# TODO: SQLAlchemy model to track stake balances and cooldowns.

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from .base import Base
from datetime import datetime

class Stake(Base):
    __tablename__ = "stakes"

    worker_pubkey = Column(String, primary_key=True)
    staked_amount = Column(Integer)
    last_staked = Column(DateTime, default=datetime.utcnow)
    pending_unstake = Column(Integer, nullable=True)
    unstake_requested_at = Column(DateTime, nullable=True)
