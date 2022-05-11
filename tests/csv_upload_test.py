#transaction upload folder test
#transaction denying uoload folder test
from app import db
from app.db.models import Transaction,User

import os

def test_transaction_upload_file(application,client):
    """ setup database user and delete """
    with application.app_context():
        user = User("beyzatest@testtest", "testtest")
        db.session.add(user)
        db.session.commit()

        root = os.path.dirname(os.path.abspath(__file__))
        filename = 'sample.csv'
        filepath = os.path.join(root, filename)

        #assert filepath == "/home/myuser/tests/sample.csv"
        assert client.get('/transactions/upload').status_code== 200


        with application.test_client(user) as client:
            with open(filepath, 'rb') as file:
                response = client.post('/transactions/upload', data=filename, follow_redirects = True)
                response = client.get('/transactions/upload')

            assert response.status_code == 200
        db.session.delete(user)


def test_denying_transaction_upload_file(application,client):
    response = client.post('/transactions/upload', data="sample.csv", follow_redirects = True)
    assert response.status_code == 400

