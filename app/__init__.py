# _*_ coding:UTF-8
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config_map
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
import logging

# 数据库
db = SQLAlchemy()

# 创建redis连接对象
# redis_store = None

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug等级
# 创建日志记录器，指明日志保存的路径，每个日志文件的最大容量、保存日志文件个数的上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志的记录格式
formatter = logging.Formatter("%(levelname)s %(filename)s %(lineno)s %(message)s")  # 日志等级、输入日志信息的文件名、行数、日志信息
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name:str 配置模式的模式名（"develop","product"）
    :return:
    """
    app = Flask(__name__)
    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    # 初始化redis工具
    # global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask_session，将session数据保存到redis中
    Session(app)

    # 为flask补充csrf防护
    CSRFProtect(app)

    # 注册蓝图
    from app.user import user as user_blueprint
    from app.apply import apply as apply_blueprint
    from app.approve import approve as approve_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(apply_blueprint, url_prefix="/apply")
    app.register_blueprint(approve_blueprint, url_prefix="/approve")

    # 404
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404


    return app

