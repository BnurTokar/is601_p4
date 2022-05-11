#test for transaction db balance
#test for transaction db query

from app import db
from app.db.models import Transaction
from calculator import Calculator

def test_transaction_balance(application):
    calculator_obj = Calculator()
    transaction1 = Transaction("100", "CREDIT", "100")
    db.session.add(transaction1)
    db.session.commit()
    balance = calculator_obj.add(transaction1.amount)
    assert balance == 100

    transaction2 = Transaction("80", "CREDIT", balance)
    db.session.add(transaction2)
    db.session.commit()
    balance = calculator_obj.add(transaction2.amount)
    assert balance == 180

    transaction3 = Transaction("-20", "DEBIT", balance)
    db.session.add(transaction3)
    db.session.commit()
    balance = calculator_obj.add(transaction3.amount)
    assert balance == 160

    db.session.delete(transaction1)
    db.session.delete(transaction2)
    db.session.delete(transaction3)


def test_transaction_query(application):
    calculator_obj = Calculator()
    transaction1 = Transaction("100", "CREDIT", "100")
    db.session.add(transaction1)
    db.session.commit()
    balance = calculator_obj.add(transaction1.amount)
    assert balance == 100
    assert db.session.query(Transaction).count() == 1


    transaction2 = Transaction("80", "CREDIT", balance)
    db.session.add(transaction2)
    db.session.commit()
    balance = calculator_obj.add(transaction2.amount)
    assert balance == 180
    assert db.session.query(Transaction).count() == 2


    transaction3 = Transaction("-20", "DEBIT", balance)
    db.session.add(transaction3)
    db.session.commit()
    balance = calculator_obj.add(transaction3.amount)
    assert balance == 160
    assert  db.session.query(Transaction).count() == 3
    db.session.delete(transaction1)
    db.session.delete(transaction2)
    db.session.delete(transaction3)
    assert  db.session.query(Transaction).count() == 0



