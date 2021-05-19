from sqlalchemy import Table, Column, Integer, String, DateTime, sql
from .base import metadata


users = Table(
    "groups", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("name", String),
    Column("created_at", DateTime, default=sql.now, nullable=False),
    Column("updated_at", DateTime, default=sql.now, nullable=False)
)