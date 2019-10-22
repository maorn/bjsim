'''
Created on Oct 10, 2019

@author: maor
'''
import bjsim.stats.game_stats as stats


def test_dealer_stats():
    stats.dealer_stats_for_given_hand(5000, 6)
    stats.player_stats(5000, 6)
    stats.player_stats(5000, 6)
