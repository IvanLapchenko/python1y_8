from flask import render_template, redirect, request
from .db_communicate import add_new_group, get_all_groups, delete_group, get_student_in_group
from . import app


@app.route('/')
@app.route('/group')
def group():
    return render_template('group_manage.html', list_of_group=get_all_groups())


@app.route('/add_group', methods=['POST'])
def add_group():
    group_name = request.form['group_name']
    print(group_name)
    add_new_group(group_name)
    return redirect('/')


@app.route('/delete_group', methods=['POST'])
def delete_group_by():
    group_name = request.form['delete_selected']
    print(group_name)
    delete_group(group_name)
    return redirect('/')


@app.route('/student/<group_name>')
def student(group_name):
    return render_template("student_manage.html", student_list=get_student_in_group(group_name))
# ORM - object relational mapping
