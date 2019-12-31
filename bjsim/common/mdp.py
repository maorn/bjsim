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
        prb = {}
        for dc in range(11):
            prb[dc] = {}
            for key, val in self.actions.items():
                prob = 1 / len(val)
                prb[dc][key] = {}
                for item in val:
                    prb[dc][key][item] = prob
        return prb

    def reset_counters(self):
        cnt = {}
        # dealer cards
        for dc in range(11):
            cnt[dc] = {}
            for key, val in self.actions.items():
                cnt[dc][key] = {}
                for item in val:
                    # making the start different from zero and if we didn't reach there we
                    # will put low probability
                    cnt[dc][key][item] = {'count': 0.001, 'reward': 0.000001}
        return cnt

    def add_game(self, final_hand, reward):

        for action in final_hand.actions:
            dc = action['dealer']
            idx = convert_hand_to_index(action['hand'])
            act = action['action']
            current = self.actions_couters[dc][idx][act]
            current['count'] = current['count'] + abs(reward)
            # count only good moves, the bad moves just counted
            if reward > 0:
                current = self.actions_couters[dc][idx][act]
                current['reward'] = current['reward'] + reward

        return

    def update_probs(self):
        for dc in range(11):
            for key, val in self.actions.items():
                norm_factor = 0
                for item in val:
                    curr = self.actions_couters[dc][key][item]
                    curr['avg'] = curr['reward'] / curr['count']
                    norm_factor = norm_factor + curr['avg']

                # update probs
                for item in val:
                    self.actions_probs[dc][key][item] = self.actions_couters[dc][key][item]['avg'] / norm_factor

        self.actions_couters = self.reset_counters()
