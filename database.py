import contextlib
from typing import AsyncIterator
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base
from config import DB_CONFIG

Base = declarative_base()

class DatabaseSessionManager:
    def __init__(self):
        pass

session_manager = DatabaseSessionManager(DB_CONFIG, {"echo": True})
        