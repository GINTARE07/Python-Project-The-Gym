from db.run_sql import run_sql
from models.member import Member
from models.session import Session

import repositories.session_repository as session_repository 


def save(member):
    sql = "INSERT INTO members (full_name, membership_type) VALUES (%s, %s) RETURNING id"
    values = [member.full_name, member.membership_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        
        member = Member(result["full_name"],result["membership_type"], result['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        member = Member(result["full_name"], result["membership_type"], result["id"])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(member):
    sql = "UPDATE members SET (full_name, membership_type) = (%s, %s) WHERE id = %s"
    values = [member.full_name, member.membership_type, member.id]
    run_sql(sql, values)