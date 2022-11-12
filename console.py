import pdb
from models.member import Member
from models.session import Session

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

# member_repository.delete_all()
# session_repository.delete_all()

member1 = Member("John Johnston", "Basic")
member_repository.save(member1)

member2 = Member("Marie Juke", "Basic")
member_repository.save(member2)

member3 = Member("Natasha Jones", "Premium")
member_repository.save(member3)

member4 = Member("Gilbert Anderson", "Premium")
member_repository.save(member4)

member5 = Member("Daisy Kelpes", "Basic")
member_repository.save(member5)


session1 = Session("Pump", 30, "Morning")
session_repository.save(session1)

session2 = Session("Cycle", 30, "Morning")
session_repository.save(session2)

session3 = Session("Yoga", 30, "Afternoon")
session_repository.save(session1)

session4 = Session("Step", 45, "Evening")
session_repository.save(session4)

session5 = Session("Burn it", 25, "Afternoon")
session_repository.save(session5)

for member in member_repository.select_all():
    print(member.__dict__)

for session in session_repository.select_all():
    print(session.__dict__)


pdb.set_trace()