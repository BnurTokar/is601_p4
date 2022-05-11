"""A simple flask web app"""
import flask_login
import os
import datetime
import time

from flask import g, request
from rfc3339 import rfc3339

from flask import render_template, Flask, has_request_context, request
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from app.auth import auth
from app.auth import auth
from app.transactions import transactions
from app.cli import create_database
from app.context_processors import utility_text_processors
from app.db import db,database
from app.config_logging import logging_config

from app.db.models import User
from app.exceptions import http_exceptions
from app.simple_pages import simple_pages
import logging
from flask.logging import default_handler

login_manager = flask_login.LoginManager()


def page_not_found(e):
    return render_template("404.html"), 404


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.register_blueprint(database)
    app.register_blueprint(logging_config)
    app.context_processor(utility_text_processors)
    app.register_blueprint(transactions)
    app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'Simplex'
    app.register_error_handler(404, page_not_found)
    # app.add_url_rule("/", endpoint="index")
    DB_DIR = os.getenv('DB_DIR','database')
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASE_DIR, '..', DB_DIR, "db.sqlite")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['WTF_CSRF_METHODS'] = []
    db.init_app(app)

    # add command function to cli commands
    app.cli.add_command(create_database)

    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))

    # set the name of the transaction uploads folder
    upload_dir = os.path.join(root, 'uploads')
    # make a directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)

    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
