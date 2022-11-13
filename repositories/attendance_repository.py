from db.run_sql import run_sql
from models.member import Member
from models.session import Session
from models.attendance import Attendance

import repositories.session_repository as session_repository 
import repositories.member_repository as member_repository


def save(attendance):
    sql = "INSERT INTO attendance (members_id, sessions_id) VALUES (%s, %s) RETURNING *"
    values = [attendance.member.id, attendance.session.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    attendance.id = id
    

def select_all():
    attendances = []

    sql = "SELECT * FROM attendance"
    results = run_sql(sql)
    for result in results:
       member = member_repository.select(result["members_id"])
       session = session_repository.select(result["sessions_id"])
       attendance = Attendance(member, session, result["id"])
       attendances.append(attendance)
    return attendances


def select(id):

    sql = "SELECT * FROM attendance WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        member = member_repository.select(result["members_id"])
        session = session_repository.select(result["sessions_id"])
        attendance = Attendance(member, session, result["id"])
     
    return attendance

# def delete_all():
#     sql = "DELETE FROM members"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM members WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(member):
#     sql = "UPDATE members SET (full_name, membership_type) = (%s, %s) WHERE id = %s"
#     values = [member.full_name, member.membership_type, member.id]
#     run_sql(sql, values)