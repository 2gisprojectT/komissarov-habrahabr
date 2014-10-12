__author__ = 'jk'
# -*- coding: utf-8 -*-


# Базовый класс
class Action(object):
    def __init__(self, name):
        self.name = name

    # Выполнить действие
    def execute(self):
        pass


# Съесть
class EatA(Action):
    def __init__(self):
        super(EatA, self).__init__('Eat')

    def execute(self):
        print 'Action: ' + self.name


# Спать
class SleepA(Action):
    def __init__(self):
        super(SleepA, self).__init__('Sleep')

    def execute(self):
        print 'Action: ' + self.name


# Бежать
class RunA(Action):
    def __init__(self):
        super(RunA, self).__init__('Run')

    def execute(self):
        print 'Action: ' + self.name


# Посмотреть
class LookA(Action):
    def __init__(self):
        super(LookA, self).__init__('Look')

    def execute(self):
        print 'Action: ' + self.name


# Статические поля
eat = EatA()
sleep = SleepA()
run = RunA()
look = LookA()

