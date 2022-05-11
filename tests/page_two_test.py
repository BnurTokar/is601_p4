# dashboard: accessing, denying; status codes
# other user auth pages: accessing; status codes
from app import db
from app.db.models import User


def test_for_accessing_dashboard(application,client):
    with application.app_context():
        assert db.session.query(User).count() == 0

        user = User('beyzatest@test.com', 'testtest')
        db.session.add(user)
        assert user.email == 'beyzatest@test.com'
        db.session.commit()

        assert db.session.query(User).count() == 1

        with application.test_client() as client:
            client.post('/login', data=dict(email='testuser@test.com', password='testtest'), follow_redirects=True)
            response_dashboard = client.get('/dashboard')

        assert response_dashboard.status_code == 302

        db.session.delete(user)
        assert db.session.query(User).count() == 0


