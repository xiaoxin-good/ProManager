# _*_ coding:UTF-8
import redis


class Config(object):
    """配置信息"""

    SECRET_KEY = "ef9609e477c8423f9bd242a4e0e64315"

    # 数据库
    DB = "mysql"
    DRIVER = "pymysql"
    NAME = "root"
    PWD = "root"
    HOST = "192.168.48.135"
    PORT = 3306
    DB_NAME = "promanager"
    CHARSET = "utf8"

    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset={}&autocommit=true".format(DB, DRIVER, NAME, PWD,
                                                                                         HOST, PORT, DB_NAME, CHARSET)
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "192.168.48.135"
    REDIS_PORT = 6379

    # flask_session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中的session进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期（单位秒）


class DevelopmentConfig(Config):
    """开发模式配置信息"""
    DEBUG = True


class ProductConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}
