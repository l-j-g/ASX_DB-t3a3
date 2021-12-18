from flask import Blueprint, jsonify, request, render_template
from main import db
from models.usage import Usage
from schemas.usage_schema import usage_schema

home = Blueprint('home', __name__)


@home.route('/home')
def display_homepage():
    data = {
        "page_title": "Home Page",
        "usage": usage_schema.dump(Usage.query.get(1))
    }
    return render_template("home.html", page_data=data)
