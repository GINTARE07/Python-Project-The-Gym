from flask import Blueprint, Flask, redirect, render_template, request

from models.attendance import Attendance
import repositories.attendance_repository as attendance_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository


attendance_blueprint = Blueprint("attendances", __name__)

# INDEX
@attendance_blueprint.route("/attendances")
def attendance():
    attendance = attendance_repository.select_all()
    return render_template("attendances/index.html", attendance=attendance)

# # NEW
# @members_blueprint.route("attendance"/new")
# def new_attendance():
#     return render_template("/attendance/new.html")

# CREATE
@attendance_blueprint.route("/attendances", methods=["POST"])
def create_attendance():
    member = member_repository.select(request.form["members_id"])
    session = session_repository.select(request.form["sessions_id"])
    new_attendance = Attendance(member, session)
    attendance_repository.save(new_attendance)
    return redirect("/attendances")

# # EDIT
# @members_blueprint.route("/members/<id>/edit")
# def edit_member(id):
#     member = member_repository.select(id)
#     return render_template('members/edit.html', member = member)

# # UPDATE

# @members_blueprint.route("/members/<id>", methods=["POST"])
# def update_member(id):

#     full_name = request.form["full_name"]
#     membership_type = request.form["membership_type"]
#     member = Member(full_name, membership_type, id)
#     member_repository.update(member)
#     return redirect("/members")

# # DELETE

# @members_blueprint.route("/members/<id>/delete", methods=["POST"])
# def delete_member(id):
#     member_repository.delete(id)
#     return redirect("/members")

# # find member by id

# @members_blueprint.route("/members/<id>")
# def view_member(id):
#     show_member = member_repository.select(id)
#     return render_template('member/show_member.html', member=show_member, bite_victims = bite_victims)
