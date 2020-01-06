# _*_ coding:UTF-8
from app.models import User, Position, Type
from app.user.decorations import login_require

from . import user
from app import db, models
from flask import current_app, render_template, request, redirect, Flask, session, Response, url_for
import json
import jsonpickle


@user.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        # 查询职位表
        positions = Position.query.all()
        return render_template('register.html', positions=positions)
    else:
        # 查询职位表
        positions = Position.query.all()
        # 接收用户数据
        workid = request.form.get('workid')
        username = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        position_id = request.form.get('position_id')
        pwd = request.form.get('password')
        repwd = request.form.get('repassword')
        # 验证用户数据
        if not all([workid, username, email, phone, position_id, pwd, repwd]):
            msg = '数据不完整'
            return render_template('register.html', msg=msg, positions=positions)
        work = User.query.filter_by(work_id=workid).first()
        if work:
            msg = '工号已存在'
            return render_template('register.html', msg=msg, positions=positions)
        emai = User.query.filter_by(email=email).first()
        if emai:
            msg = '邮箱已存在'
            return render_template('register.html', msg=msg, positions=positions)
        phon = User.query.filter_by(phone=phone).first()
        if phon:
            msg = '手机号已存在'
            return render_template('register.html', msg=msg, positions=positions)
        if pwd != repwd:
            msg = '密码不一致'
            return render_template('register.html', msg=msg, positions=positions)
        # 存储用户数据

        user = User(
            work_id=workid,
            name=username,
            email=email,
            phone=phone,
            face=None,
            position_id=position_id,
            pwd=pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user.login"))


@user.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        contact = request.cookies.get('contact')
        if contact:
            pwd = request.cookies.get('pwd')
            return render_template('login.html', contact=contact, pwd=pwd)
        return render_template('login.html')
    else:
        # 获取用户数据
        contact = request.form.get('contact')
        pwd = request.form.get('password')
        remember = request.form.get('remember')
        # 验证用户数据
        if not all(['contact', 'pwd']):
            msg = '数据不完整'
            return render_template('login.html', msg=msg)
        # 使用工号或姓名登陆
        user = User.query.filter_by(work_id=contact, pwd=pwd).first()
        if not user:
            user = User.query.filter_by(name=contact, pwd=pwd).first()
        if user:
            # 正则表达式判断是用户名，邮箱，手机
            # if re
            # 存储session
            session["user"] = jsonpickle.dumps(user)
        # 存储cookie

        response = redirect(url_for("user.index"))
        if remember == 'on':
            response.set_cookie('contact', contact)
            response.set_cookie('pwd', pwd)
            return response
        else:
            response.delete_cookie('contact')
            response.delete_cookie('pwd')
        # 用户登录主页
        return response


# 项目管理主页
@login_require
@user.route("/")
def index():
    user = session.get('user')
    user = jsonpickle.loads(user)
    return render_template('index.html', user=user)


@user.route("/logout/")
def logout():
    session.pop('user')
    return redirect(url_for(("user.login")))


@user.route("/addtype/", methods=["POST", "GET"])
@login_require
def addtype():
    if request.method == "GET":
        user = session.get('user')
        user = jsonpickle.loads(user)
        return render_template('addtype.html', user=user)
    else:
        # 接收数据
        # typeid=request.form.get('typeid')
        typename = request.form.get('typename')
        # 验证数据
        if not all([typename]):
            msg = "数据不完整"
            return render_template('addtype.html', msg=msg)
        type1 = Type.query.filter_by(name=typename).first()
        if type1:
            msg = "改项目类别已存在"
            return render_template('addtype.html', msg=msg)
        # 存储数据
        type = Type(
            name=typename
        )
        db.session.add(type)
        db.session.commit()
        return render_template('addtype.html')
