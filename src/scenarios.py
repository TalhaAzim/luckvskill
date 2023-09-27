from agents import SimpleAgent
import random
from aggregate_analysis import AggregateAnalysis


def constant_value(value):

    def param_fn(tick):
        return value

    return param_fn


def random_value(pad, scale):

    #value = pad + random.random() * scale

    def param_fn(tick):
        return pad + random.random() * scale

    return param_fn

class SkillLevel(object):

    def __init__(self, level):
        self.level = level

    def __call__(self, tick):
        return (self.level - 1) + random.random()

class FixedSkillLevel(object):

    def __init__(self, level):
        self.level = level

    def __call__(self, tick):
        return self.level