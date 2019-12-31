'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.mdp import start_game
from bjsim.common.cards import BjDeck
from bjsim.common.game import play_hand, play_game
from bjsim.common.policies import random_policy
from bjsim.common.globals import HAND_OPTIONS


def test_states():
    actions_probs, actions_counter = start_game()
    policy_params = {'actions': HAND_OPTIONS}

    for i in range(10000):
        deck = BjDeck(6)
        final_hand, d_hand, rewards = play_game(deck, [1], random_policy, **policy_params)
        print(1)
