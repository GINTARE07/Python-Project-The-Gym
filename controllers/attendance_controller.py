from flask import Blueprint, Flask, redirect, render_template, request

from models.attendance import Attendance
import repositories.attendance_repository as attendance_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository


attendance_blueprint = Blueprint("attendances", __name__)

# INDEX
@attendance_blueprint.route("/attendances")
def attendance():
    attendances = attendance_repository.select_all()
    return render_template("attendances/index.html", attendances=attendances)

# NEW
@attendance_blueprint.route("/attendances/new", methods=["GET"])
def new_attendance():
    # get all members
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("/attendances/new.html", members=members, sessions=sessions)

# CREATE
@attendance_blueprint.route("/attendances/new", methods=["POST"])
def create_attendance():
    member = request.form["member_id"]
    session = request.form["session_id"]
    new_attendance = Attendance(member, session)
    attendance_repository.save(new_attendance)
    return redirect("/attendances")

# EDIT
@attendance_blueprint.route("/attendances/<id>/edit", methods=["GET"])
def edit_attendance(id):
    attendance = attendance_repository.select(id)
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("attendances/edit.html", attendance = attendance, members = members, sessions = sessions)

# UPDATE

@attendance_blueprint.route("/attendances/<id>", methods=["POST"])
def updated_attendance(id):

    member = member_repository.select(request.form["member_id"])
    session = session_repository.select(request.form["session_id"])
    updated_attendance = Attendance(member, session, id)
    attendance_repository.update(updated_attendance)
    return redirect("/attendances")
