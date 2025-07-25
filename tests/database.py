from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import get_db, Base
from alembic import command

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# Create the SQLAlchemy engine (connect sqlalchemy to the database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # alembic method for running running the test client (testing the routes and requests) with a new database each time
# @pytest.fixture
# def client():
#     # run our code after the test finishes
#     command.upgrade("head")
#     # run our code before we run our test
#     command.downgrade("base")
#     yield TestClient(app)


# sqlalchemy method for running running the test client (testing the routes and requests) with a new database each time

@pytest.fixture
def session():
    # run our code after the test finishes
    Base.metadata.drop_all(bind=engine)
    # run our code before we run our test
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    # get a database session (connection to the database)
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)