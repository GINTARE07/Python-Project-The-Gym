import unittest


from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member ("John Johnston", "Basic")



    def test_member_has_membership(self):
        self.assertEqual("Basic", self.member.membership_type)

    # # @unittest.skip("delete this line to run the test")
    # def test_member_name(self):
    #     result = member_name(self.member_repository.full_name)
    #     self.assertEqual(self.member.full_name)