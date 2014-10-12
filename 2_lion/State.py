__author__ = 'jk'
# -*- coding: utf-8 -*-


# Базовый класс сотояния
class State(object):
    def __init__(self, name):
        self.name = name

    def message(self):
        print 'State: ' + self.name


# Голодный
class HungryS(State):
    def __init__(self):
        super(HungryS, self).__init__('Hungry')


# Сытый
class FullS(State):
    def __init__(self):
        super(FullS, self).__init__('Full')


# Статические поля
hungry = HungryS()
full = FullS()