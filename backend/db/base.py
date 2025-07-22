# base.py
# TODO: Define SQLAlchemy base class and engine init.

from sqlalchemy.ext.declarative import declarative_base

# TODO: Instantiate declarative base
Base = declarative_base()

# TODO: Define common mixins if needed (timestamped, UUID, etc.)
