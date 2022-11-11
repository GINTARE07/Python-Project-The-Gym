from flask import Blueprint, Flask, render_template
from repositories import session_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", all_sessions=sessions)

# NEW

# CREATE
# EDIT
# UPDATE
# DELETE