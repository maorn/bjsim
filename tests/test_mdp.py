'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.mdp import MDP
from bjsim.common.cards import BjDeck
from bjsim.common.game import play_game
from bjsim.common.policies import random_policy
from bjsim.common.globals import HAND_OPTIONS


def test_states():
    markov = MDP(HAND_OPTIONS)
    policy_params = {'actions': markov.actions}
    deck = BjDeck(6)
    for i in range(10000):

        deck.start_game()
        final_hand, d_hand, rewards = play_game(deck, [1], random_policy, **policy_params)
        markov.add_game(final_hand[0], rewards[0])
        print(i)
