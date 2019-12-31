'''
Created on Nov 5, 2019

@author: maor
'''
from bjsim.common.mdp import MDP
from bjsim.common.cards import BjDeck
from bjsim.common.game import play_game
from bjsim.common.policies import random_policy, max_policy,\
    probability_based_policy
from bjsim.common.globals import HAND_OPTIONS


def test_states():
    markov = MDP(HAND_OPTIONS)
    policy_params = {'actions': markov.actions,
                     'actions_prob': markov.actions_probs,
                     'threshold': 90}
    deck = BjDeck(6)
    start_money = 0
    end_money = start_money
    for games in range(10000):

        deck.start_game()
        final_hand, d_hand, rewards = play_game(deck, [1], random_policy, **policy_params)
        end_money = end_money + rewards[0]
        markov.add_game(final_hand[0], rewards[0])
    curr_win = (end_money - start_money) / games
    print("average win/lost per game: ", curr_win)

    past_win = -1000
    while(curr_win > past_win):
        past_win = curr_win
        markov.update_probs()
        start_money = 0
        end_money = start_money
        policy_params = {'actions': markov.actions,
                         'actions_prob': markov.actions_probs,
                         'threshold': 90}
        for games in range(100000):

            deck.start_game()
            final_hand, d_hand, rewards = play_game(
                deck, [1], probability_based_policy, **policy_params)
            end_money = end_money + rewards[0]
            markov.add_game(final_hand[0], rewards[0])
        curr_win = (end_money - start_money) / games
        print("average win/lost per game: ", curr_win)

    print(markov.actions_probs)
