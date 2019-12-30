'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.mdp import start_game
from bjsim.common.cards import BjDeck
from bjsim.common.game import play_hand
from bjsim.common.policies import random_policy


def test_states():
    actions, actions_probs, actions_counter = start_game()
    policy_params = {'actions': actions}
    for state in actions:
        for i in range(10000):
            deck = BjDeck(6)
            player = [state]
            dealer = [deck.deal()]
            bet = 1
            a = play_hand(player, dealer[0], deck, bet, random_policy, **policy_params)

        print(state)
