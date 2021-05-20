import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime
from .base import metadata


groups = Table(
    "groups", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("name", String),
    Column("created_at", DateTime, default=datetime.datetime.utcnow(), nullable=False),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow(), nullable=False)
)
