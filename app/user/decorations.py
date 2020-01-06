from functools import wraps

import jsonpickle
from flask import redirect, session, url_for, request


# 定义登录装饰器
def login_require(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("user.login", next=request.url))
        return func(*args, **kwargs)

    return inner


