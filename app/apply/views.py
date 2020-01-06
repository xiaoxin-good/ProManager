# _*_ coding:UTF-8
from app.apply.forms import ProForm
from app.models import Area, AddPro, Type, User, Status
from . import apply
from app import db
from flask import render_template, flash, redirect, url_for, request


# 新增项目计划
@apply.route("/pro/add/", methods=["get", "post"])
def pro_add():
    form = ProForm()

    if request.method:
        form.area_id.choices = [(v.id, v.name) for v in Area.query.order_by("id").all()]
        form.type_id.choices = [(v.id, v.name) for v in Type.query.all()]
        form.check_id.choices = [(v.id, v.name) for v in User.query.all()]
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(id=data["user_id"]).first_or_404()
        pro_count = AddPro.query.filter_by(name=data['title']).count()
        proID_count = AddPro.query.filter_by(pro_id=data["proID"]).count()
        if pro_count == 1:
            flash("该项目计划已经存在！", "err")
            return redirect(url_for("apply.pro_add"))
        if proID_count == 1:
            flash("该项目计划编号已经存在！", "err")
            return redirect(url_for("apply.pro_add"))
        pro = AddPro(
            pro_id=data["proID"],
            name=data["title"],
            type_id=data["type_id"],
            area_id=data["area_id"],
            user_id=data["user_id"],
            phone=data["phone"],
            expected_start_time=data["start_time1"],
            actual_strat_time=data["start_time2"],
            expected_completion_time=data["end_time1"],
            actual_completion_time=data["end_time2"],
            status_id=1,
            check_id=data["check_id"],
            budget=data["budget"],
        )
        db.session.add(pro)
        db.session.commit()
        flash("新增项目成功", "OK")
        return redirect(url_for("apply.pro_add"))
    return render_template("pro_add.html", form=form)


# 项目计划列表
@apply.route("/pro/list/<int:page>/", methods=["get", "post"])
def pro_list(page=None):
    if page is None:
        page = 1
    # page_data = AddPro.query.join(Type).join(Area).join(Status).join(User).filter(
    #     Type.id == AddPro.type_id,
    #     Area.id == AddPro.area_id,
    #     Status.id == AddPro.status_id,
    #     User.id == AddPro.check_id
    # ).order_by(AddPro.addtime.desc()).paginate(page=page, per_page=2)
    page_data = AddPro.query.order_by(AddPro.addtime.desc()).paginate(page=page, per_page=2)
    return render_template('pro_list.html', page_data=page_data)


# 修改项目
@apply.route("/pro/edit/<int:id>/", methods=["get", "post"])
def pro_edit(id):
    form = ProForm()
    pro = AddPro.query.get_or_404(id)
    if request.method:
        form.area_id.choices = [(v.id, v.name) for v in Area.query.order_by("id").all()]
        form.type_id.choices = [(v.id, v.name) for v in Type.query.all()]
        form.check_id.choices = [(v.id, v.name) for v in User.query.all()]
    if request.method == "GET":
        form.type_id.data = pro.type_id
        form.area_id.data = pro.area_id
        form.check_id.data = pro.check_id

    if form.validate_on_submit():
        data = form.data
        pro_count = AddPro.query.filter_by(name=data['title']).count()
        proID_count = AddPro.query.filter_by(pro_id=data["proID"]).count()
        if pro.name != data["title"] and pro_count == 1:
            flash("该项目计划已经存在！", "err")
            return redirect(url_for("apply.pro_edit", id=id))
        if pro.pro_id != data["proID"] and proID_count == 1:
            flash("该项目计划编号已经存在！", "err")
            return redirect(url_for("apply.pro_edit", id=id))

        pro.pro_id = data["proID"],
        pro.name = data["title"],
        pro.type_id = data["type_id"],
        pro.area_id = data["area_id"],
        pro.user_id = data["user_id"],
        pro.phone = data["phone"],
        pro.expected_start_time = data["start_time1"],
        pro.actual_strat_time = data["start_time2"],
        pro.expected_completion_time = data["end_time1"],
        pro.actual_completion_time = data["end_time2"],
        pro.check_id = data["check_id"],
        pro.budget = data["budget"],

        db.session.add(pro)
        db.session.commit()
        flash("修改项目计划成功！", "OK")

        return redirect(url_for("apply.pro_edit", id=id))
    return render_template('pro_edit.html', form=form, pro=pro)


# 项目计划提交
@apply.route("/pro/commit/<int:id>/", methods=["get"])
def pro_commit(id=None):
    pro = AddPro.query.filter_by(id=id).first_or_404()
    pro.status_id = 2
    db.session.add(pro)
    db.session.commit()
    flash("提交项目成功！", "OK")
    return redirect(url_for("apply.pro_list", page=1))


# 删除项目计划
@apply.route("/pro/del/<int:id>/", methods=['get'])
def pro_del(id=None):
    pro = AddPro.query.filter_by(id=id).first_or_404()
    db.session.delete(pro)
    db.session.commit()
    flash("删除项目成功！", "OK")
    return redirect(url_for("apply.pro_list", page=1))

# 项目计划详情页
@apply.route("/pro/detail/<string:pro_id>/")
def detail(pro_id):
    pro_detail = AddPro.query.filter_by(pro_id=pro_id).first()
    return render_template('pro_detail.html', pro=pro_detail)
