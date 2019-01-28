import unittest
from app import fun


class AppTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("login")
		cls.user="Samba"

	@classmethod
	def tearDownClass(cls):
		print("logout")
		cls.user=None
	def setUp(self):
		print("reserving the resource:r1")

	def tearDown(self):
		print("releasing the resource:r1")


	def test_10_20(self):
		print("running test_10_20: %s"%self.user)
		
		res = fun(10,20)
		exp = 30
		self.assertEqual(res,exp,"test_10_20 failed")
		
	def parsing(self):
		

		print("this is parsing")
	def test_s1_s2(self):
		print("running test_s1_s2 %s"%self.user)
		
		res=fun("s1","s2")
		exp="s1s2"
		self.assertEqual(res,exp,"test_s1_s2 failed")
		
	def test_s1_20(self):
		print("running test_s1_20 %s"%self.user)
		res=fun("s1",20)
		exp=None
		self.assertEqual(res,exp,"test_s1_20 failed")
		
	def test_10_s2(self):
		print("running test_10_s2: %s"%self.user)
		res=fun(10,"s2")
		exp=None
		self.assertEqual(res,exp,"test_10_s2 failed")
		
unittest.main()