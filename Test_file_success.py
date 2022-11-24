#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from main_prog import divide

class TestDivide(unittest.TestCase):

	def test_3(self):
		x3 = 100
		y3 = 100
		result = divide(x3, y3)
		self.assertEqual(result, 1)

	def test_4(self):
		x4 = 0
		y4 = 50
		result = divide(x4, y4)
		self.assertEqual(result, 0)

	def test_5(self):
		x5 = 100
		y5 = 5
		result = divide(x5, y5)
		self.assertEqual(result, 20)

if __name__ == '__main__':
	unittest.main()
