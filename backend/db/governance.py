# governance.py
# TODO: SQLAlchemy models for proposals and voting.

from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, Enum
from .base import Base
import enum

class ProposalStatus(enum.Enum):
    ACTIVE = "active"
    PASSED = "passed"
    REJECTED = "rejected"

class Proposal(Base):
    __tablename__ = "proposals"

    proposal_id = Column(String, primary_key=True)
    creator_pubkey = Column(String)
    title = Column(String)
    description_uri = Column(String)
    options = Column(String)  # JSON or comma-separated list
    vote_counts = Column(String)  # JSON or serialized
    status = Column(Enum(ProposalStatus), default=ProposalStatus.ACTIVE)
    start_ts = Column(DateTime)
    end_ts = Column(DateTime)

class Vote(Base):
    __tablename__ = "votes"

    id = Column(String, primary_key=True)
    voter_pubkey = Column(String)
    proposal_id = Column(String, ForeignKey("proposals.proposal_id"))
    selected_option = Column(Integer)
    weight = Column(Integer)
    has_voted = Column(Boolean, default=False)
