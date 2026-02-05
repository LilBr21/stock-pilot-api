# TODO: Configure pytest fixtures
#
# Key fixtures to implement:
#
# import pytest
# from httpx import AsyncClient, ASGITransport
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
#
# from app.main import app
# from app.db.base import Base
# from app.db.session import get_async_session
#
# # Use SQLite for tests (in-memory)
# TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
#
# @pytest.fixture
# async def async_engine():
#     engine = create_async_engine(TEST_DATABASE_URL, echo=False)
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield engine
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#     await engine.dispose()
#
# @pytest.fixture
# async def db_session(async_engine):
#     async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
#     async with async_session() as session:
#         yield session
#
# @pytest.fixture
# async def client(db_session):
#     async def override_get_db():
#         yield db_session
#
#     app.dependency_overrides[get_async_session] = override_get_db
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
#         yield ac
#     app.dependency_overrides.clear()
