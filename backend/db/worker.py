# worker.py
# TODO: SQLAlchemy model for registered compute workers.

from sqlalchemy import Column, String, Boolean, Integer, DateTime
from .base import Base
from datetime import datetime

class Worker(Base):
    __tablename__ = "workers"

    pubkey = Column(String, primary_key=True)  # Wallet address
    metadata_uri = Column(String)
    zk_pubkey_hash = Column(String)  # 32-byte hex
    reputation_score = Column(Integer, default=0)
    active = Column(Boolean, default=True)
    last_seen = Column(DateTime, default=datetime.utcnow)
