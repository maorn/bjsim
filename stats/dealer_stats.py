'''
Created on Oct 8, 2019

@author: maor
'''
import pandas as pd
from common.cards import BjDeck, count_hand
from common.game import dealer_hand


def dealer_stats_for_given_hand(games=1000000, decks=6, save_fn=None):
    dealer_stats = {}
    for i in range(1, 11):
        dealer_stats[str(i)] = {'17': 0, '18': 0, '19': 0, '20': 0, '21': 0, 'F': 0}

    for _ in range(games):
        deck = BjDeck(decks)
        start_hand = deck.deal()
        dealer = [start_hand]
        d_cards = dealer_hand(dealer, deck)
        count = count_hand(d_cards)
        if count > 21:
            count = 'F'
        dealer_stats[str(start_hand)][str(count)] = dealer_stats[str(start_hand)][str(count)] + 1.
    raw_count = pd.DataFrame(dealer_stats)
    print(raw_count)
    total = raw_count / raw_count.sum(axis=0)
    print(total)
    if save_fn is not None:
        raw_count.to_csv(save_fn + 'count.csv')
        total.to_csv(save_fn + 'percent.csv')
