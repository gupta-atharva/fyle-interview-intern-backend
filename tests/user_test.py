import pytest
from core import db
from core.models.users import User
from datetime import datetime

@pytest.fixture
def new_user():
    return User(username='testuser', email='testuser@example.com')

def test_user_model(test_client, new_user):
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()

        retrieved_user = User.query.get(new_user.id)
        assert retrieved_user is not None
        assert retrieved_user.username == 'testuser'
        assert retrieved_user.email == 'testuser@example.com'
        assert isinstance(retrieved_user.created_at, datetime)
        assert isinstance(retrieved_user.updated_at, datetime)
        
        expected_repr = f"<User 'testuser'>"
        assert retrieved_user.__repr__() == expected_repr

def test_user_filter(test_client, new_user):
    with test_client.application.app_context():

        users = User.filter(User.username == 'testuser').all()
        assert len(users) == 1
        assert users[0].username == 'testuser'

def test_user_get_by_email(test_client, new_user):
    with test_client.application.app_context():

        user = User.get_by_email(new_user.email)
        assert user is not None
        assert user.email == 'testuser@example.com'
