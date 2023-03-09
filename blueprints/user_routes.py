from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

user_pages = Blueprint('user_pages', __name__, template_folder='templates')

@user_pages.route('/', defaults={'page': 'index'})
@user_pages.route('/<page>')
def index(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)