__author__ = 'jk'
# -*- coding: utf-8 -*-
import Action as a
import InputObject as o
import State as s


# Класс автомата льва
class Lion:
    def __init__(self, state):
        if not isinstance(state, s.State):
            raise ValueError('Wrong state')
        self.action = None
        self.state = state
        # Таблица состояний и действий
        self.automate = {
            (s.full, o.antelope): (s.hungry, a.sleep),
            (s.full, o.hunter): (s.hungry, a.run),
            (s.full, o.tree): (s.hungry, a.look),
            (s.hungry, o.antelope): (s.full, a.eat),
            (s.hungry, o.hunter): (None, a.run),
            (s.hungry, o.tree): (None, a.sleep)}

    # Обработка встреченного объекта
    def meet(self, instance):
        if not isinstance(instance, o.InputObject):
            raise ValueError('Wrong input object')
        if (self.state, instance) not in self.automate:
            raise ValueError('Wrong combination of object and state')
        state, action = self.automate[(self.state, instance)]
        if state is not None:
            self.state = state
        if action is not None:
            self.action = action
            self.action.execute()