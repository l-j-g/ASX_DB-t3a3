from flask import Blueprint, jsonify, request, render_template
from main import db

home = Blueprint('home', __name__)


@home.route('/home')
def display_homepage():
    data = {
        "page_title": "ASX Data - Home Page",
    }
    return render_template("home.html", page_data=data)
