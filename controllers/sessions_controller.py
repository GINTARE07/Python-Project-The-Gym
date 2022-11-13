from flask import Blueprint, Flask, render_template, redirect, request

from models.session import Session
from repositories import session_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)

# NEW
@sessions_blueprint.route("/sessions/new")
def new_member():
    return render_template("/sessions/new.html")


# EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_member(id):
    sessions = session_repository.select(id)
    return render_template("sessions/edit.html", session = sessions)

# UPDATE

@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    part_of_day = request.form["part of day"]
    capacity = request.form["capacity"]
    session = Session(name, part_of_day, capacity, id)
    session_repository.update(session)
    return redirect("/sessions")

# CREATE
# EDIT
# UPDATE
# DELETE