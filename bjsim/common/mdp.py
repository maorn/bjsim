'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.globals import HAND_OPTIONS


def init_equal_probs(actions: dict):
    actions_probs = {}
    for key, val in actions.items():
        prob = 1 / len(val)
        actions_probs[key] = {}
        for item in val:
            actions_probs[key][item] = prob
    return actions_probs


def init_counters(actions: dict):
    actions_couters = {}
    for key, val in actions.items():
        actions_couters[key] = {}
        for item in val:
            actions_couters[key][item] = {'count': 0, 'reward': 0}
    return actions_couters


def start_game():
    actions_probs = init_equal_probs(HAND_OPTIONS)
    actions_counter = init_counters(HAND_OPTIONS)
    return actions_probs, actions_counter
