# job.py
# TODO: SQLAlchemy model for compute job lifecycle and zk proof tracking.

from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey
from .base import Base
from datetime import datetime
import enum

class JobStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SLASHED = "slashed"
    CANCELLED = "cancelled"

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(String, primary_key=True)
    client_pubkey = Column(String)
    worker_pubkey = Column(String, ForeignKey("workers.pubkey"))
    job_hash = Column(String)
    proof_hash = Column(String, nullable=True)
    funded_amount = Column(Integer)
    status = Column(Enum(JobStatus), default=JobStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
