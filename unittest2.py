#!/usr/bin/python3
import unittest
from primality import Primality

class Testcases(unittest.TestCase):
	def tc1(self):
		self.assertEqual(Primality(100),True)
	def tc2(self):
		self.assertEqual(Primality(-67),True)
	def tc3(self):
		self.assertEqual(Primality(43),False)
	def tc4(self):
		self.assertEqual(Primality(1),True)

if __name__ == '__main__':
	unittest.main()