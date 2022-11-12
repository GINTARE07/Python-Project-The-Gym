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
    for row in results:
        
        session = Session(row["name"],row["capacity"], row['part_of_day'])
        sessions.append(session)
    return sessions