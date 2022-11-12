from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members", methods = ["GET"])
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

# # NEW
# @members_blueprint.route("/members/new")
# def new_member():
#     return render_template("/members/new.html")

# # CREATE
# @members_blueprint.route("/members", methods=["POST"])
# def create_member():
#     first_name = request.form["first_name"]
#     last_name = request.form["last_name"]
#     membership_type = request.form["membership_type"]
#     new_member = Member(first_name, last_name, membership_type)
#     member_repository.save(new_member)
#     return redirect("/members")

# EDIT

# UPDATE

# DELETE

# find member by id

# @members_blueprint.route("/members/<id>")
# def view_member(id):
#     show_member = member_repository.select(id)
#     return render_template('member/show_member.html', member=show_member, bite_victims = bite_victims)
