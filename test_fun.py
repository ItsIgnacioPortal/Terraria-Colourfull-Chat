import unittest
from unittest import mock
import fun

#for color tests
from colour import Color

#for monitor selector tests
from screeninfo import get_monitors
from monitor_settings import *

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
		

	@mock.patch('fun.input', create=True)
	def test_modifyGradientColor(self, mocked_input):
		
		#"a" will print out an error
		#"1" will select "Active gradient color"
		#"69" will try to select an invalid color, and return with the original colours

		mocked_input.side_effect = ["a", 1, "69"]
		result = fun.modifyGradientColor(Color("red"),Color("blue"))
		self.assertEqual(result, [Color("red"),Color("blue")])


		#"True" will print out an error
		#"2" will select "Target gradient color"
		#"#fffff?" will try to select an invalid color, and return an array of the original colors

		mocked_input.side_effect = [True, 2, "#fffff?"]
		result = fun.modifyGradientColor(Color("red"),Color("blue"))
		self.assertEqual(result, [Color("red"),Color("blue")])


		#"-4" will print out an error
		#"2" will select "Target gradient color"
		#"#ffffff" will select white, and return an array with red and white

		mocked_input.side_effect = [-4, 2, "#ffffff"]
		result = fun.modifyGradientColor(Color("red"),Color("blue"))
		self.assertEqual(result, [Color("red"),Color("white")])
	

	@mock.patch('fun.input', create=True)
	def test_getMonitorConf(self, mocked_input):

		#heightOfMainMonitor read from monitor_settings.py
		#widthOfMainMonitor read from monitor_settings.py
		try:
			middleCoordinates = [widthOfMainMonitor / 2, heightOfMainMonitor / 2]
		except:
			print("[TEST SUITE]: You must modify the value of two variables on this test to suit your IRL monitor setup. (monitor number 1, according to windows)\nThis script assumes that monitor number 1 is on the center of your setup (ignore if you only have one monitor)")
			raise ValueError

		#Get the monitor count
		#monitorCount = len(monitors)
		monitors = []
		for monitor in get_monitors():
			monitors.append(monitor)

		#"a" will print out an error
		#"True" will print out an error
		#"0" will print out an error
		#"-1" will print out an error
		#"1" will select the first avalible monitor
		#"a" will print out an error
		#"True" will print out an error
		#"0" will print out an error
		#"center" will select the "center" location.
		# An array will be returned with the center coordinates of the selected monitor.

		mocked_input.side_effect = ["a", True, 0, -1, 1, "a", True, 0, "center"]
		#Prioritize legibility
		result = fun.getMonitorConf()
		self.assertEqual(result, middleCoordinates)
	

if __name__ == "__main__":
	unittest.main()
