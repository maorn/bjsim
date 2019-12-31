'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.policies import convert_hand_to_index


class MDP:

    def __init__(self, actions: dict):
        self.actions = actions
        self.actions_probs = self.init_equal_probs()
        self.actions_couters = self.reset_counters()

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
                # making the start different from zero
                actions_couters[key][item] = {'count': 0.0001, 'reward': 0.0001}
        return actions_couters

    def add_game(self, final_hand, reward):
        for action in final_hand.actions:
            idx = convert_hand_to_index(action['hand'])
            act = action['action']
            self.actions_couters[idx][act]['count'] = self.actions_couters[idx][act]['count'] + 1
            # count only good moves, the bad moves just counted
            if reward > 0:
                self.actions_couters[idx][act]['reward'] = self.actions_couters[idx][act]['reward'] + reward
        return

    def update_probs(self):
        for key, val in self.actions.items():
            norm_factor = 0
            for item in val:
                curr = self.actions_couters[key][item]
                curr['avg'] = curr['reward'] / curr['count']
                norm_factor = norm_factor + curr['avg']

            # update probs
            for item in val:
                self.actions_probs[key][item] = self.actions_couters[key][item]['avg'] / norm_factor

        self.actions_couters = self.reset_counters()
