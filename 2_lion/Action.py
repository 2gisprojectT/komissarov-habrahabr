__author__ = 'jk'
# -*- coding: utf-8 -*-


# Базовый класс
class Action:
    def __init__(self, name):
        self.name = name

    # Выполнить действие
    def execute(self):
        pass


# Съесть
class EatA(Action):
    def __int__(self):
        super(self).__init__('Eat')

    def execute(self):
        print 'Action: ' + self.name


# Спать
class SleepA(Action):
    def __int__(self):
        super(self).__init__('Sleep')

    def execute(self):
        print 'Action: ' + self.name


# Бежать
class RunA(Action):
    def __int__(self):
        super(self).__init__('Run')

    def execute(self):
        print 'Action: ' + self.name


# Посмотреть
class LookA(Action):
    def __int__(self):
        super(self).__init__('Look')

    def execute(self):
        print 'Action: ' + self.name


# Статические поля
eat = EatA()
sleep = SleepA()
run = RunA()
look = LookA()

