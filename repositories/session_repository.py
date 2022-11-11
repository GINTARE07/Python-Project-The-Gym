from db.run_sql import run_sql
from models.session import Session

def save(session):
    sql = "INSERT INTO sessions (name, capacity, part_of_day) VALUES (%s, %s, %s) RETURNING id"
    values = [session.name, session.capacity, session.part_of_day]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id