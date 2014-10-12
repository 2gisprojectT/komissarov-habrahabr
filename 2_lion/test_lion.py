__author__ = 'jk'
# -*- coding: utf-8 -*-
import Action as a
import InputObject as o
import State as s
import Lion as l
import unittest


class MyTestCase(unittest.TestCase):
    def test_lion_creation(self):
        try:
            lion = l.Lion(s.hungry)
            self.assertEqual(s.hungry, lion.state, 'Wrong state of created lion')
        except ValueError:
            self.fail("Exception during lion creation")
        try:
            lion = l.Lion(s.full)
            self.assertEqual(s.full, lion.state, 'Wrong state of created lion')
        except ValueError:
            self.fail("Exception during lion creation")


if __name__ == '__main__':
    unittest.main()
