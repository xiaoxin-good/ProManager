# _*_ coding:UTF-8
from flask import Blueprint

# 创建蓝图对象
approve = Blueprint("approve", __name__)

# 导入蓝图的视图
from app.approve import views
