from flask import Blueprint, Flask, render_template, request, redirect
from repositories import member_repository
from models.member import Member

members_blueprint = Blueprint("members", __name__)

# INDEX

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("member/index.html", members=members)

# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("/members/new.html")
# CREATE

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    membership_type = request.form["membership_type"]
    new_member = Member(first_name, last_name, membership_type)
    member_repository.save(new_member)
    return redirect("/members")

# EDIT
# UPDATE
# DELETE