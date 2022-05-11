# This page tests:
# - user db query
# - transactions attached to a user
# - transactions column

from app import db
from app.db.models import User, Transaction

def test_user_query(application):
    with application.app_context():

        assert db.session.query(User).count() == 0
        email = 'beyzatest@test.com'
        password = 'testtest'
        user = User(email, password)
        db.session.add(user)

        user = User.query.filter_by(email=email).first()

        assert user.email == email
        assert db.session.query(User).count() == 1

        db.session.delete(user)
        assert db.session.query(User).count() == 0


def test_user_transaction_query(application):
    with application.app_context():

        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0

        email = 'beyzatest@test.com'
        password = 'testtest'
        user = User(email, password)

        db.session.add(user)
        assert db.session.query(User).count() == 1

        user.transactions = [Transaction("100", "CREDIT", "100"), Transaction("200", "DEBIT", "100")]
        assert db.session.query(Transaction).count() == 2

        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0

