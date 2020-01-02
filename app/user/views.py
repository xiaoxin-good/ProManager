# _*_ coding:UTF-8
from . import user
from app import db, models
from flask import current_app,render_template


@user.route("/register")
def index():
    return render_template('index.html')
