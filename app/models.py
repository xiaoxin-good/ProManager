# _*_ coding:UTF-8
from datetime import datetime
from werkzeug.security import check_password_hash

from app import db


# 用户
class User(db.Model):
    """用户模块"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    work_id = db.Column(db.String(5), unique=True)  # 工号
    name = db.Column(db.String(100))  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机
    face = db.Column(db.String(255), unique=True)  # 头像
    status = db.Column(db.Integer, default=1)  # 激活状态，默认激活，状态为1
    # position_id = db.Column(db.Integer, db.ForeignKey("position.id"))  # 所属职位
    position_id = db.Column(db.Integer, default=1)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # position_name = db.relationship("Position")  # 职位外键关系关联


    def __repr__(self):
        return "<User {}>".format(self.name)

    # 密码验证
    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


class Position(db.Model):
    """职位表"""
    __tablename__ = "position"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 职位名称
    grade = db.Column(db.Integer, unique=True)  # 职位等级


# users = db.relationship("User", backref="position")  # 用户外键关系关联


def __repr__(self):
    return "<Position {}>".format(self.name)


class Type(db.Model):
    """项目类别模块"""
    __tablename__ = "type"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 项目类别名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Type {}>".format(self.name)


class Area(db.Model):
    """省份表"""
    __tablename__ = "area"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 省份名称

    def __repr__(self):
        return "<Area {}>".format(self.name)


class AddPro(db.Model):
    """新增项目计划模块"""
    __tablename__ = "add_pro"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pro_id = db.Column(db.String(100), unique=True)  # 项目编号
    type_id = db.Column(db.Integer, db.ForeignKey("type.id"))  # 所属项目类型
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(100), unique=True)  # 项目名称
    area_id = db.Column(db.Integer, db.ForeignKey("area.id"))  # 所属省份
    phone = db.Column(db.String(11))  # 联系电话
    expected_start_time = db.Column(db.DateTime)  # 预计启动时间
    actual_strat_time = db.Column(db.DateTime)  # 实际启动时间
    expected_completion_time = db.Column(db.DateTime)  # 预计结束时间
    actual_completion_time = db.Column(db.DateTime)  # 实际结束时间
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"), default=1)  # 所属状态
    budget = db.Column(db.Float)  # 总预算
    check_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 选择审批人
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    type = db.relationship('Type')  # 类别外键关系关联
    area = db.relationship("Area")  # 省份外键关系关联
    status = db.relationship("Status")  # 状态外键关系关联
    check = db.relationship("User")  # 审批人外键关系关联

    # user = db.relationship("User",foreign_keys="user_id",extend_existing=True)

    def __repr__(self):
        return "<AddPro {}>".format(self.name)


class Status(db.Model):
    """状态表"""
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 状态名称

    def __repr__(self):
        return "<Status {}>".format(self.name)


class Check(db.Model):
    """项目审核模块"""
    __tablename__ = "check"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pro_id = db.Column(db.Integer, db.ForeignKey("add_pro.id"))  # 所属项目
    result = db.Column(db.Enum('同意', '修改', '驳回'), default="同意", nullable=False)  # 审批结果
    suggestion = db.Column(db.Text, nullable=True)  # 审批意见
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属审批人
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Check {}>".format(self.result)
