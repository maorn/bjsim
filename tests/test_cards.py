'''
Created on Oct 8, 2019

@author: maor
'''
from bjsim.common.cards import count_hand, BjDeck
from bjsim.common.game import play_game
from bjsim.common.policies import convert_hand_to_index, fixed_policy
from bjsim.common.globals import WEB_POLICY


def test_counts():
    assert count_hand([1, 1, 1, 1, 10]) == 14
    assert count_hand([1, 10, 1, 10]) == 22
    assert count_hand([8, 1]) == 19
    assert count_hand([1, 10]) == 21
    assert count_hand([1, 1]) == 12


def test_policy():
    policy = fixed_policy([4, 2, 4], 6, WEB_POLICY)
    assert policy == 'H'


def test_game():
    b = BjDeck(6)
    policy_params = {'policy': WEB_POLICY}
    a, b, c = play_game(b, [100], fixed_policy, **policy_params)
    print(a, b, c)


def test_index():
    index = convert_hand_to_index([1, 3])
    index2 = convert_hand_to_index([3, 1])
    assert index == index2
