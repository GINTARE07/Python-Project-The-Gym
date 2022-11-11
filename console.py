import pdb
from models.member import Member
from models.session import Session

from repositories import  member_repository, session_repository

# member_repository.delete_all()

member1 = Member("John", "Johnston", "Basic")
member_repository.save(member1)

member2 = Member("Marie", "Juke", "Basic")
member_repository.save(member2)

member3 = Member("Natasha", "Jones", "Premium")
member_repository.save(member3)

member4 = Member("Gilbert", "Anderson", "Premium")
member_repository.save(member4)

member5 = Member("Daisy", "Kelpes", "Basic")
member_repository.save(member5)


session1 = Session("Pupm", 30, "Morning")
session_repository.save(session1)


pdb.set_trace()