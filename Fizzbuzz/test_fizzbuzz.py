import unittest
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    """ Testing fizzbuzz """

    def test_if_three_is_fizz(self):
        """Test if three returns fizz"""
        self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz',
                         msg='Three should return fizz')

    def test_if_five_is_buzz(self):
        """Test if five returns buzz"""
        self.assertEqual(fizzbuzz.fizz_buzz(5), 'buzz',
                         msg='Five should return buzz')

    def test_if_fifteen_is_fizzbuzz(self):
        """Test if fifteen returns fizzbuzz"""
        self.assertEqual(fizzbuzz.fizz_buzz(15), 'fizzbuzz',
                         msg='Fifteen should return fizzbuzz')

    def test_if_ninety_nine_is_fizz(self):
        """Test if ninety nine returns fizz"""
        self.assertEqual(fizzbuzz.fizz_buzz(99), 'fizz',
                         msg='Ninety nine should return fizz')

    def test_if_one_hundred_is_buzz(self):
        """Test if ome hundred returns buzz"""
        self.assertEqual(fizzbuzz.fizz_buzz(100), 'buzz',
                         msg='One hundred should return buzz')

    def test_if_sixty_is_fizzbuzz(self):
        """Test if sixty returns fizzbuzz"""
        self.assertEqual(fizzbuzz.fizz_buzz(60), 'fizzbuzz',
                         msg='Sixty should return fizzbuzz')

    def test_returns_buzz(self):
        """Returns buzz if the input is divisible by five"""
        self.assertEqual(fizzbuzz.fizz_buzz(10), 'buzz',
                         msg='Ten should return buzz')

    def test_returns_fizz(self):
        """Returns fizz if the input is divisible by three"""
        self.assertEqual(fizzbuzz.fizz_buzz(21), 'fizz',
                         msg='Twenty one should return buzz')

    def test_returns_fizzbuzz(self):
        """Returns fizzbuzz if the input is divisible by fifteen"""
        self.assertEqual(fizzbuzz.fizz_buzz(45), 'fizzbuzz',
                         msg='Forty five should return fizzbuzz')

    def test_if_zero_returns_zero(self):
        """Returns zero if the input is zero"""
        self.assertEqual(fizzbuzz.fizz_buzz(0), 0,
                         msg='Zero should return zero')

    def test_return_number_if_not_fizz_buzz_or_fizzbuzz(self):
        """Returns number if the number is not fizz, buzz or fizzbuzz """
        self.assertEqual(fizzbuzz.fizz_buzz(109), 109,
                         msg='109 should return 109')

    def test_for_negative_numbers(self):
        """Raise error if the input is negative"""
        with self.assertRaises(Exception):
            self.fizzbuzz.fizz_buzz(-3)

    def test_for_non_integers(self):
        """Raise error if the input is not an integer"""
        with self.assertRaises(TypeError):
            fizzbuzz.fizz_buzz('j')

    def test_for_null_value(self):
        """Raise error if no argument is passed"""
        with self.assertRaises(Exception):
            fizzbuzz.fizz_buzz('')


if __name__ == '__main__':
    unittest.main()
