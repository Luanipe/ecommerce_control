import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.core.dependencies import get_db_session

from main import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db_session] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_token(client):
    client.post("/api/v1/auth/register", json={
        "username": "test.user",
        "name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "password": "123456"
    })

    response = client.post("/api/v1/auth/login", data={
        "username": "test.user",
        "password": "123456"
    })

    assert response.status_code == 200
    token = response.json()["access_token"]
    return token
