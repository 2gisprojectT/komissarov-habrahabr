__author__ = 'jk'
# -*- coding: utf-8 -*-
import Action as a
import InputObject as o
import State as s
import Lion as l
import random as r
import unittest

automate = {(s.full, o.antelope): (s.hungry, a.sleep),
            (s.full, o.hunter): (s.hungry, a.run),
            (s.full, o.tree): (s.hungry, a.look),
            (s.hungry, o.antelope): (s.full, a.eat),
            (s.hungry, o.hunter): (s.hungry, a.run),
            (s.hungry, o.tree): (s.hungry, a.sleep)}
inputs = [o.antelope, o.hunter, o.tree]
states = [s.hungry, s.full]


class LionTest(unittest.TestCase):
    # Создание льва
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

    # Создание льва с ошибочными параметрами
    def test_lion_wrong_creation(self):
        self.assertRaises(ValueError, l.Lion, None)
        self.assertRaises(ValueError, l.Lion, object)

    # Подача корректных объектов
    def test_input_objects(self):

        lion = l.Lion(s.hungry)
        try:
            for i in range(0, 50):
                j = r.randint(0, len(inputs) - 1)
                lion.meet(inputs[j])
        except:
            self.fail('Exception on correct input')

    # Подача некорректных объектов
    def test_input_wrong_objects(self):
        objects = [None, 55, a.eat, object]
        lion = l.Lion(s.hungry)
        for i in objects:
            self.assertRaises(ValueError, lion.meet, i)

    # Проверка правильности перехода по состояниям
    def test_states(self):
        for state in states:
            for input_object in inputs:
                lion = l.Lion(state)
                lion.meet(input_object)
                true_state, none = automate[(state, input_object)]
                self.assertEqual(true_state, lion.state, 'Wrong lion state')

    # Проверка правильности реакции на объекты
    def test_actions(self):
        for state in states:
            for input_object in inputs:
                lion = l.Lion(state)
                lion.meet(input_object)
                none, true_action = automate[(state, input_object)]
                self.assertEqual(true_action, lion.action, 'Wrong lion state')


if __name__ == '__main__':
    unittest.main()
