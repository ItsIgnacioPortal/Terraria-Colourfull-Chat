import unittest
from unittest import mock
import fun

class TestMain(unittest.TestCase):
	#https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
	@mock.patch('fun.input', create=True)
	def test_selectWorkingMode(self,  mocked_input):
		
		#"a" will print out an error, and then "1" will succeed. "2" will succeed too.
		mocked_input.side_effect = ["a", "1", "2"]
		
		#Prioritize legibility
		result = fun.selectWorkingMode()
		self.assertIn(result, [1, 2])
		result = fun.selectWorkingMode()
		self.assertIn(result, [1, 2])


	

if __name__ == "__main__":
	unittest.main()
