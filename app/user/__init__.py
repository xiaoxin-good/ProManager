# _*_ coding:UTF-8
from flask import Blueprint

# 创建蓝图对象
index = Blueprint("user",__name__)

# 导入蓝图的视图
from app.user import views