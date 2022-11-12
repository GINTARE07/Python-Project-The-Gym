from db.run_sql import run_sql
from models.member import Member
from models.session import Session

import repositories.session_repository as session_repository 


def save(member):
    sql = "INSERT INTO members (full_name, membership_type) VALUES (%s, %s) RETURNING *"
    values = [member.full_name, member.membership_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        
        member = Member(row["full_name"],row["membership_type"], row['id'])
        members.append(member)
    return members


# def select(id):
#     sql = "SELECT * FROM members WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
#     # Could alternativly have..
#     # if len(results) > 0 
#     if results:
#         result = results[0]
#         # zombie_type = zombie_type_repository.select(result["zombie_type_id"])
#         member = Member(result["first_name"],result["last_name"], result["membership_type"], result["id"])
#     return member