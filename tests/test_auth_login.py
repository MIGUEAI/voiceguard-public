import json
from app import app, db
from models.user import User
from werkzeug.security import generate_password_hash

def setup_module(module):
    with app.app_context():
        db.drop_all()
        db.create_all()
        user = User(
            name="Test User",
            email="testuser@example.com",
            password=generate_password_hash("test123")
        )
        db.session.add(user)
        db.session.commit()

def test_login_success():
    with app.test_client() as client:
        response = client.post(
            "/users/login",
            data=json.dumps({"email": "testuser@example.com", "password": "test123"}),
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert "access_token" in data

def test_login_failure():
    with app.test_client() as client:
        response = client.post(
            "/users/login",
            data=json.dumps({"email": "testuser@example.com", "password": "wrongpass"}),
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 401
        assert data["msg"] == "Credenciais inválidas"

