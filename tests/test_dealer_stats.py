'''
Created on Oct 10, 2019

@author: maor
'''
from bjsim.common.game_stats import dealer_stats_for_given_hand


def test_dealer_stats():
    dealer_stats_for_given_hand(5000, 6)
