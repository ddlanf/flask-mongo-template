from flask import Blueprint, render_template
from .extensions import mongo

main = Blueprint('main', __name__,)

@main.route('/')
def index():
    return render_template('index.html')