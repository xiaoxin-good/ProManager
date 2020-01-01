# _*_ coding:UTF-8
from . import approve
from app import db, models
from flask import current_app


@approve.route("/abc")
def index():
    current_app.logger.error("1")
    current_app.logger.warn("2")
    current_app.logger.info("3")
    current_app.logger.debug("4")
    return "user page"
