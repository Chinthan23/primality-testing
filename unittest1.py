#!/usr/bin/python3

import unittest
from primality import Primality

class Testcases(unittest.TestCase):
	def tc1(self):
		self.assertEqual(Primality(2),True)
	def tc2(self):
		self.assertEqual(Primality(-67),False)
	def tc3(self):
		self.assertEqual(Primality(37),True)
	def tc4(self):
		self.assertEqual(Primality(1),False)

if __name__ == '__main__':
	unittest.main()