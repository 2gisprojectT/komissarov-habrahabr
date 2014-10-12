__author__ = 'jk'
# -*- coding: utf-8 -*-


# Базовый класс сотояния
class State:
    def __init__(self, name):
        self.name = name

    def message(self):
        print 'State: ' + self.name


# Голодный
class HungryS(State):
    def __int__(self):
        super(self).__init__('Hungry')


# Сытый
class FullS(State):
    def __int__(self):
        super(self).__init__('Full')


# Статические поля
hungry = HungryS()
full = FullS()