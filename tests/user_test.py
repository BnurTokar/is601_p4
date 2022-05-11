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


def test_user_transaction_column(application):
    with application.app_context():

        email = 'beyzatest@test.com'
        password = 'testtest'
        user = User(email, password)
        db.session.add(user)
        user = User.query.filter_by(email=email).first()

        assert user.email == email
        assert db.session.query(User).count() == 1

        user.transactions = [Transaction("100", "CREDIT", "100"), Transaction("200", "DEBIT", "300"), Transaction("500", "DEBIT", "800")]

        transaction1 = Transaction.query.filter_by(amount='100').first()
        assert transaction1.type == "CREDIT"
        assert transaction1.balance == "100"

        transaction2 = Transaction.query.filter_by(amount='200').first()
        assert transaction2.type == "DEBIT"
        assert transaction2.balance == "300"

        transaction3 = Transaction.query.filter_by(amount='500').first()
        assert transaction3.type == "DEBIT"
        assert transaction3.balance == "800"
        db.session.delete(user)