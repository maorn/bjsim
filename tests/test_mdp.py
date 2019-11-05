'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.mdp import build_states, init_probs


def test_states():
    actions = build_states()
    init_probs(actions)
