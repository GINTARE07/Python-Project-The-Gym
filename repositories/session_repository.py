from db.run_sql import run_sql
from models.session import Session
from models.member import Member

import repositories.member_repository as member_repository

def save(session):
    sql = "INSERT INTO sessions (name, capacity, part_of_day) VALUES (%s, %s, %s) RETURNING *"
    values = [session.name, session.capacity, session.part_of_day]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id
    return session


def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for result in results:
        
        session = Session(result["name"], result["capacity"], result["part_of_day"], result["id"])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        session = Session(result["name"], result["part_of_day"], result["capacity"], result["id"])
    return session

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(session):
    sql = "UPDATE sessions SET (name, part_of_day, capacity) = (%s, %s, %s) WHERE id = %s"
    values = [session.name, session.part_of_day, session.capacity, session.id]
    run_sql(sql, values)