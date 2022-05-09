import os
import logging
import flask

from flask import has_request_context, request
from logging.config import dictConfig
from app import config

logging_config = flask.Blueprint('logging_config', __name__)

class RequestFormat(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
            record.request_method = request.method
            record.request_path = request.path
            record.args = dict(request.args)
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)

@logging_config.after_app_request
def logging_after_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    return response
    request_log = logging.getLogger("each_request_response.log")
    request_log.debug("Request log after app request")


@logging_config.before_app_first_request
def logging_before_request():
    # set the name of the apps log folder to logs
    logdir = config.Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logging.config.dictConfig(LOGGING_CONFIG)
    request_log = logging.getLogger("each_request_response")
    request_log.debug("Request log before app request")


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'RequestFormatter': {
            '()': 'app.config_logging.RequestFormat',
            'format': '%(levelname)s : %(message)s method: %(request_method)s , route: %(request_path)s , [%(asctime)s] , request address: %(remote_addr)s'
        }

    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'handler.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.upload_csv': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'app/logs/upload_transaction.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.each_request_response': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'RequestFormatter',
            'filename': 'app/logs/each_request_response.log',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default','file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default','file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'uploadCsv': {  # if __name__ == '__main__'
            'handlers': ['file.handler.upload_csv'],
            'level': 'DEBUG',
            'propagate': False
        },
        'eachRequestResponse': {  # if __name__ == '__main__'
            'handlers': ['file.handler.each_request_response'],
            'level': 'DEBUG',
            'propagate': False
        },

    }
}
