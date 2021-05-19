import os
from databases import Database
from sqlalchemy import create_engine, MetaData, Column, Integer, String, DateTime, Table

DATABASE_URL = os.getenv("IS_SOFT_DATABASE_URL")

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
