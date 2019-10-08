'''
Created on Oct 8, 2019

@author: maor
'''
from common.cards import count_hand, BjDeck, dealer_hand, final_money, init_game
import pandas as pd
from common.globals import STANDARD_LOGIC


def test_counts():
    assert count_hand([1, 1, 1, 1, 10]) == 14
    assert count_hand([1, 10, 1, 10]) == 22
    assert count_hand([8, 1]) == 19
    assert count_hand([1, 10]) == 21
    assert count_hand([1, 1]) == 12


def test_money():
    ret = final_money([16, 17, 18, 19, 20, 21, 22, 25], 18, 5)
    print(ret)


def test_init_game():
    deck = BjDeck(8)
    player, dealer = init_game(3, deck)
    print(player, dealer)
    print(STANDARD_LOGIC)
