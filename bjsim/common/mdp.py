'''
Created on Nov 5, 2019

@author: maor
'''


class MDP:

    def __init__(self, actions: dict):
        self.actions = actions
        self.actions_probs = self.init_equal_probs()
        self.actions_counter = self.reset_counters()

    def init_equal_probs(self):
        actions_probs = {}
        for key, val in self.actions.items():
            prob = 1 / len(val)
            actions_probs[key] = {}
            for item in val:
                actions_probs[key][item] = prob
        return actions_probs

    def reset_counters(self):
        actions_couters = {}
        for key, val in self.actions.items():
            actions_couters[key] = {}
            for item in val:
                actions_couters[key][item] = {'count': 0, 'reward': 0}
        return actions_couters

    def add_game(self, final_hand, rewards):
        return
