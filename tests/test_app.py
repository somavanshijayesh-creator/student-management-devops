
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.routes import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Management System" in response.data


def test_add_student(client):
    response = client.post(
        "/add",
        data={
            "name": "Rahul Patil",
            "email": "rahul@example.com",
            "course": "Computer Science",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Rahul Patil" in response.data
    assert b"rahul@example.com" in response.data
