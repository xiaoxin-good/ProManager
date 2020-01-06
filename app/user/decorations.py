from functools import wraps

from flask import redirect, session, url_for, request


def login_require(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("user.login", next=request.url))
        return func(*args, **kwargs)

    return inner

# def admin_login_req(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if "user" not in session:
#             return redirect(url_for("user.login", next=request.url))
#         return f(*args, **kwargs)
#
#     return decorated_function
