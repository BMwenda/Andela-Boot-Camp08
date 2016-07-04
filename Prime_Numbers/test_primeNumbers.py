'''Module for testing function for getting 1st n primes'''
import unittest
import primeNumbers


class Test_Prime_Numbers(unittest.TestCase):
    '''A class for get_primes() function tests'''

    def test_for_zero(self):
        '''Test if zero  returns empty list'''
        self.assertEqual(primeNumbers.get_primes(0), [],
                         msg="Zero should return empty list")

    def test_for_one(self):
        '''Test for the first prime number'''
        self.assertEqual(primeNumbers.get_primes(
            1), [2], msg="One should return [2]")

    def test_for_two(self):
        '''Test for the first two primes'''
        self.assertEqual(primeNumbers.get_primes(
            2), [2, 3], msg="Two should return [2,3]")

    def test_first_five_primes(self):
        '''Test the first five prime numbers'''
        self.assertEqual(primeNumbers.get_primes(
            5), [2, 3, 5, 7, 11], msg="Five should return [2, 3, 5, 7, 11]")

    def test_negative_numbers(self):
        '''Test that negative numbers are not allowed'''
        with self.assertRaises(Exception):
            primeNumbers.get_primes(-5)

    def test_non_integers(self):
        '''Test that non-integer data types are not accepted'''
        with self.assertRaises(TypeError):
            primeNumbers.get_primes('t')

if __name__ == '__main__':
    unittest.main()
