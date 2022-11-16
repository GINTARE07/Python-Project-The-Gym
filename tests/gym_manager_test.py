import unittest
from repositories.attendance_repository import *
from repositories.member_repository import *
from repositories.session_repository import *

class TestMember_repository(unittest.TestCase):
    def setUp(self):
        self.member.full_name = []
        self.member.membership_type = ["Basic", "Premium"]
        self.member.id = None
    
    # @unittest.skip("delete this line to run the test")
    def test_member_name(self):
        result = member_name(self.member_repository.full_name)
        self.assertEqual(self.member.full_name)