from sqlalchemy.sql import func
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from .base import metadata


users = Table(
    "users", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("name", String),
    Column("surname", String),
    Column("groups_id", Integer, ForeignKey('groups.id'), nullable=False),
    Column("created_at", DateTime, default=func.now(), nullable=False),
    Column("updated_at", DateTime, default=func.now(), nullable=False)
)
