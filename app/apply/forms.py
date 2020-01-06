# _*_ coding:UTF-8
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired


class ProForm(FlaskForm):
    """项目管理表单"""

    proID = StringField(
        label="项目编号",
        validators=[
            DataRequired("请输入项目编号")
        ],
        description="项目编号",
        render_kw={
            "class": "form-control",
            "id": "input_ProID",
            "placeholder": "请输入项目编号",
            "required": False,
        }
    )
    title = StringField(
        label="项目名称",
        validators=[
            DataRequired("请输入项目名称")
        ],
        description="项目名称",
        render_kw={
            "class": "form-control",
            "id": "input_ProID",
            "placeholder": "请输入项目名称",
            "required": False,
        }
    )
    type_id = SelectField(
        label="所属类别",
        validators=[
            DataRequired("请选择类别")
        ],
        description="所属类别",
        coerce=int,
        choices="",
        render_kw={
            "class": "form-control",
            "required": False,
        }
    )

    area_id = SelectField(
        label="承担省份",
        validators=[
            DataRequired("请选择省份")
        ],
        description="承担省份",
        coerce=int,
        choices="",
        render_kw={
            "class": "form-control",
            "required": False,
        }
    )
    user_id = IntegerField(
        label="负责人",
        validators=[
            DataRequired("请输入负责人")
        ],
        description="负责人",
        render_kw={
            "class": "form-control",
            "id": "input_user",
            "placeholder": 1,
            "required": False,
        }
    )

    phone = StringField(
        label="联系电话",
        validators=[
            DataRequired("请输入联系电话")
        ],
        description="联系电话",
        render_kw={
            "class": "form-control",
            "id": "input_user",
            "placeholder": "请输入联系电话",
            "required": False,
        }
    )
    start_time1 = StringField(
        label="预计启动时间",
        validators=[
            DataRequired("请选择启动时间")
        ],
        description="预计启动时间",
        render_kw={
            "class": "form-control",
            "id": "input_start_time1",
            "placeholder": "请选择启动时间",
            "required": False,
        }
    )
    start_time2 = StringField(
        label="实际启动时间",
        validators=[
            DataRequired("请选择启动时间")
        ],
        description="实际启动时间",
        render_kw={
            "class": "form-control",
            "id": "input_start_time2",
            "placeholder": "请选择启动时间",
            "required": False,
        }
    )
    end_time1 = StringField(
        label="预计结束时间",
        validators=[
            DataRequired("请选择结束时间")
        ],
        description="预计结束时间",
        render_kw={
            "class": "form-control",
            "id": "input_end_time1",
            "placeholder": "请选择结束时间",
            "required": False,
        }
    )
    end_time2 = StringField(
        label="实际结束时间",
        validators=[
            DataRequired("请选择结束时间")
        ],
        description="实际结束时间",
        render_kw={
            "class": "form-control",
            "id": "input_end_time2",
            "placeholder": "请选择启动时间",
            "required": False,
        }
    )
    check_id = SelectField(
        label="审批人",
        validators=[
            DataRequired("请选择审批人")
        ],
        description="审批人",
        coerce=int,
        choices="",
        render_kw={
            "class": "form-control",
            "required": False,
        }
    )
    budget = FloatField(
        label="总预算（万元）",
        validators=[
            DataRequired("请输入总预算")
        ],
        description="总预算（万元）",
        render_kw={
            "class": "form-control",
            "id": "input_budget",
            "placeholder": "请输入总预算",
            "required": False,
        }
    )
    submit1 = SubmitField(
        "确认新增",
        render_kw={
            "class": "btn btn-primary",
        }
    )
    submit2 = SubmitField(
        "确认修改",
        render_kw={
            "class": "btn btn-primary",
        }
    )
