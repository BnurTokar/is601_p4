from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

import logging

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates')


@simple_pages.route('/')
def index():
    try:
        log = logging.getLogger("eachRequestResponse")
        log.info("opened home page")
        return render_template('index.html')
    except TemplateNotFound:
        log.info("home page 404")
        abort(404)

@simple_pages.route('/about')
def about():
    try:
        log = logging.getLogger("eachRequestResponse")
        log.info("opened about page")
        return render_template('about.html')
    except TemplateNotFound:
        log.info("about page 404")
        abort(404)
