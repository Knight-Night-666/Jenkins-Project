#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from main_prog import divide

class TestDivide(unittest.TestCase):
	def test_1(self):
		x1 = 100
		y1 = 0
		result = divide(x1, y1)
		self.assertEqual(result, -1)
		
	def test_2(self):
		x2 = 10
		y2 = 5
		result = divide(x2, y2)
		self.assertEqual(result, 50)
  

if __name__ == '__main__':
	unittest.main()
