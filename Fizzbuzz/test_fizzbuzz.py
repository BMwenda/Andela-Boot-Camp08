import unittest
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
	""" Testing fizzbuzz
	"""
	def test_returns_fizz(self):
		"""Returns fizz if the input is
			divisible by three
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(3),'fizz')

	def test_returns_buzz(self):
		"""Returns buzz if the input is
		divisible by five
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(5),'buzz')

	def test_returns_fizzbuzz(self):
		"""Returns fizzbuzz if the input is
		divisible by fifteen
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(15),'fizzbuzz')