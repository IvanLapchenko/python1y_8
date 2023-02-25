from . database import *


def add_new_group(name):
    group = Group(name=name)
    session.add(group)
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
