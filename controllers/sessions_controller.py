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
@sessions_blueprint.route("/sessions/new", methods=["GET"])
def new_session():
    return render_template("/sessions/new.html")

# CREATE
@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    capacity = request.form["capacity"]
    part_of_day = request.form["part_of_day"]
    new_session = Session(name, capacity, part_of_day)
    session_repository.save(new_session)
    return redirect("/sessions")


# EDIT
@sessions_blueprint.route("/sessions/<id>/edit", methods=["GET"])
def edit_session(id):
    sessions = session_repository.select(id)
    return render_template("sessions/edit.html", session = sessions)

# UPDATE

@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    capacity = request.form["capacity"]
    part_of_day = request.form["part_of_day"]
    session = Session(name, capacity, part_of_day, id)
    session_repository.update(session)
    return redirect("/sessions")

# DELETE

@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")


