'''
Created on Nov 5, 2019

@author: maor
'''


def build_states():
    hsd = ['H', 'S', 'D']
    hsdy = ['H', 'S', 'D', 'Y']
    actions = {'21': ['S'], 'A,10': ['S']}
    for i in range(20, 5, -1):
        actions[str(i)] = hsd
    for strt in ['A,2', 'A,3', 'A,4', 'A,5', 'A,6', 'A,7', 'A,8', 'A,9']:
        actions[strt] = hsd
    for strt in ['A,A', '2,2', '3,3', '4,4', '5,5', '6,6', '7,7', '8,8', '9,9', '10,10']:
        actions[strt] = hsdy
    return actions


def init_probs(actions: dict):
    actions_probs = {}
    for key, val in actions.items():
        length_val = 1 / len(val)
        actions_probs[key] = {}
        for item in val:
            actions_probs[key][item] = length_val
    return actions_probs


def init_counters(actions: dict):
    actions_couters = {}
    for key, val in actions.items():
        actions_couters[key] = {}
        for item in val:
            actions_couters[key][item] = {'count': 0, 'reward': 0}
    return actions_couters


def start_game():
    actions = build_states()
    actions_probs = init_probs(actions)
    actions_counter = init_counters(actions)
    return actions, actions_probs, actions_counter
