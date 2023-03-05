from .database import *
from . import login_manager


def add_new_item(obj):
    session.add(obj)
    session.commit()


def get_all_groups():
    list_ = session.query(Group).all()
    list_ = [i.name for i in list_]
    return list_


def delete_group(name):
    group_to_delete = session.query(Group).\
                      where(Group.name == name).first()
    session.delete(group_to_delete)
    session.commit()


def get_student_in_group(group):
    group_id = session.query(Group).where(Group.name == group).first().id
    list_of_students = session.query(Student).where(Student.group == group_id).all()
    list_of_students_names = [i.name for i in list_of_students]
    return list_of_students_names


def check_if_user_exist_by(username):
    return session.query(User).where(User.name == username).first()


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))
