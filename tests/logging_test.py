import os
from app import config

root = config.Config.BASE_DIR

filename_each = 'each_request_response.log'
filename_upload = 'upload_transaction.log'


def test_log_files_paths():

    filepath_each = os.path.join(root, filename_each)
    assert filepath_each == '/home/myuser/app/each_request_response.log'

    filepath_upload = os.path.join(root, filename_upload)
    assert filepath_upload == '/home/myuser/app/upload_transaction.log'

