__author__ = 'jk'
# -*- coding: utf-8 -*-


# Базовый класс входных объектов
class InputObject(object):
    def __init__(self, name):
        self.name = name


# Антилопа
class AntelopeO(InputObject):
    def __init__(self):
        super(AntelopeO, self).__init__('Antelope')


# Охотник
class HunterO(InputObject):
    def __init__(self):
        super(HunterO, self).__init__('Hunter')


# Дерево
class TreeO(InputObject):
    def __init__(self):
        super(TreeO, self).__init__('Tree')


# Статические поля
antelope = AntelopeO()
hunter = HunterO()
tree = TreeO()
