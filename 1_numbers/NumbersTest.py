__author__ = 'jk'
from unittest import TestCase
from Numbers import Numbers
import unittest
import math


class NumbersTest(TestCase):

    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEquals(1, num.a, 'A have wrong value')
        self.assertEquals(2, num.b, 'B have wrong value')
        self.assertEquals(3, num.c, 'C have wrong value')

    def test_init_negative(self):
        num = Numbers(1, 2, -3)
        self.assertEquals(1, num.a, 'A have wrong value')
        self.assertEquals(2, num.b, 'B have wrong value')
        self.assertEquals(0, num.c, 'C have wrong value')

    def test_sum(self):
        a = 1
        b = 2
        c = 3
        num = Numbers(a, b, c)
        self.assertEquals(a + b + c, num.sum(), 'Wrong sum')

    def test_multiplication(self):
        a = 1
        b = 2
        c = 3
        num = Numbers(a, b, c)
        self.assertEquals(a * b * c, num.multiplication(), 'Wrong multiplication')

    def test_abs_multiplication(self):
        a = 1
        b = -2
        c = 3
        num = Numbers(a, b, c)
        self.assertEquals(math.fabs(a * b * c), num.abs_multiplication(), 'Wrong abs_multiplication')

if __name__ == '__main__':
    unittest.main()