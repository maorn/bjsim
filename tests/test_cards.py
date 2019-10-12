'''
Created on Oct 8, 2019

@author: maor
'''
from common.cards import count_hand, BjDeck

from common.game import final_money, play_game


def test_counts():
    assert count_hand([1, 1, 1, 1, 10]) == 14
    assert count_hand([1, 10, 1, 10]) == 22
    assert count_hand([8, 1]) == 19
    assert count_hand([1, 10]) == 21
    assert count_hand([1, 1]) == 12


def test_game():
    b = BjDeck(6)
    a, b, c = play_game(b, [100])
    print(a, b, c)
