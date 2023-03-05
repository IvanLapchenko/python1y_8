from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask import render_template, redirect, request, flash
from .db_communicate import *
from . import app


def is_user_can_be_logged_in(user, password) -> bool:
    if user:
        return check_password_hash(user.password, password)
    return False


@app.route('/')
@app.route('/group')
@login_required
def group():
    return render_template('group_manage.html', list_of_group=get_all_groups())


@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route('/add_group', methods=['POST'])
def add_group():
    group_name = request.form['group_name']
    group = Group(name=group_name)
    add_new_item(group)
    return redirect('/')


@app.route('/delete_group', methods=['POST'])
def delete_group_by():
    group_name = request.form['delete_selected']
    print(group_name)
    delete_group(group_name)
    return redirect('/')


@app.route('/student/<group_name>')
@login_required
def student(group_name):
    return render_template("student_manage.html", student_list=get_student_in_group(group_name))
# ORM - object relational mapping


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        user = check_if_user_exist_by(name)

        if is_user_can_be_logged_in(user, password):
            login_user(user)
            return redirect("/group")

        flash("Check your login details and try again")
        return redirect("login")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        if check_if_user_exist_by(name):
            flash("This user already exists")
            return redirect("signup")

        password = generate_password_hash(password)
        user = User(name, password)
        add_new_item(user)
        return redirect("login")

    return render_template("signup.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("login")




