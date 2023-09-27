import random


class SimpleAgent(object):

    def __init__(self, capital, skill_fn, weight_fn):
        self.capital = capital
        self.skill_fn = skill_fn
        self.weight_fn = weight_fn

    def tick(self, tick, luck_volatility):
        #skill = 1 if random.random() < self.skill_fn(tick) else -1
        #luck = 1 if random.random() < luck_volatility else -1
        skill_wt = self.weight_fn(tick)
        #self.capital += skill * skill_wt + luck * luck_wt
        self.capital += skill_wt * (self.skill_fn(tick)) + (1 - skill_wt) * luck_volatility


class AccretionAgent(object):
    pass
