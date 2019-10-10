'''
Created on Oct 7, 2019

@author: maor
'''
import random
from common.globals import ONE_SET


def count_hand(cards):
    count = 0
    # aces need special care
    number_of_aces = 0
    for card in cards:
        if card == 1:
            number_of_aces = number_of_aces + 1
        else:
            count = count + card

    while number_of_aces > 0:
        # only one ace can be 11 and only if we below 10
        if number_of_aces > 1 or count + 11 > 21:
            count = count + 1
        else:
            count = count + 11
        number_of_aces = number_of_aces - 1

    return count


class BjDeck:
    def __init__(self, decks: int=1):
        self.deck = ONE_SET * decks
        random.shuffle(self.deck)
        self.cur_card = 0

    def deal(self):
        card = self.deck[self.cur_card]
        self.cur_card = self.cur_card + 1
        return card
