'''
Created on Oct 8, 2019

@author: maor
'''
import pandas as pd
from common.cards import BjDeck, dealer_hand


def dealer_stats_for_given_hand():
    dealer_stats = {}
    for i in range(1, 11):
        dealer_stats[str(i)] = {'17': 0, '18': 0, '19': 0, '20': 0, '21': 0, 'F': 0}

    for _ in range(1000000):
        deck = BjDeck(6)
        start_hand = deck.deal()
        dealer = [start_hand]
        count = dealer_hand(dealer, deck)
        if count > 21:
            count = 'F'
        dealer_stats[str(start_hand)][str(count)] = dealer_stats[str(start_hand)][str(count)] + 1.
    raw_count = pd.DataFrame(dealer_stats)
    raw_count.to_csv('count.csv')
    total = raw_count / raw_count.sum(axis=0)
    total.to_csv('percent.csv')
