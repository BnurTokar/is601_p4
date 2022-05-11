import os
from app import config

root = config.Config.BASE_DIR

filename_each = 'each_request_response.log'
filename_upload = 'upload_transaction.log'


def test_log_files_paths():

    filepath_each = os.path.join(root, filename_each)

    filepath_upload = os.path.join(root, filename_upload)


def test_each_request_response_log_file():

    absolute_folder = config.Config.LOG_DIR_TEST
    absolute_file = os.path.join(absolute_folder, filename_each)

    assert os.path.isfile(absolute_file)


def test_upload_transaction_log_file ():

    absolute_folder = config.Config.LOG_DIR_TEST
    absolute_file = os.path.join(absolute_folder, filename_upload)

    assert os.path.isfile(absolute_file)
