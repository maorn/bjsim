'''
Created on 2019

@author: Darya
'''
from bjsim.common.mdp import start_game


def simulate_all_games():
    actions, actions_probs, actions_counter = start_game()

    for state in actions:
        print(state)
