'''
Created on Oct 10, 2019

@author: maor
'''
import random
import pandas as pd
from bjsim.common.cards import count_hand


def policy_selector(func, **params):
    return func(**params)


def convert_hand_to_index(cards: list) -> str:
    ''' possible outcomes:
    'Y' = split
    'D' = double
    'S' = Stand
    'H' = Hit
    '''
    if len(cards) == 2:
        if cards[0] == cards[1]:
            if cards[0] == 1:
                index = 'A,A'
            else:
                index = f'{cards[0]},{cards[1]}'
        elif cards[0] == 1:
            index = f'A,{cards[1]}'
        elif cards[1] == 1:
            index = f'A,{cards[0]}'
        else:
            count = count_hand(cards)
            index = str(count)
    else:
        count = count_hand(cards)
        index = str(count)
    return index


def fixed_policy(cards: list, dealer_card: int, policy: pd.DataFrame, **_) -> str:

    if dealer_card == 1:
        dealer_str = 'A'
    else:
        dealer_str = str(dealer_card)
    index = convert_hand_to_index(cards)
    try:
        pol = policy.loc[index, dealer_str]
        if len(cards) > 2 and (pol == 'D' or pol == 'Y'):
            return 'H'
        return pol
    except BaseException:
        print(cards)


def random_policy(cards: str, actions: dict, **_)->str:
    idx = convert_hand_to_index(cards)
    rand_call = random.randint(1, len(actions[idx]))
    action = actions[idx][rand_call - 1]
    if len(cards) > 2 and (action == 'D' or action == 'Y'):
        return 'H'
    return actions[idx][rand_call - 1]


def max_policy(cards: str, actions: dict, actions_prob: dict, dealer_card: int, **_)->str:
    idx = convert_hand_to_index(cards)
    prob_values = actions_prob[dealer_card][idx].values()
    action = actions[idx][list(prob_values).index(max(prob_values))]
    if len(cards) > 2 and (action == 'D' or action == 'Y'):
        return 'H'
    return action


def probability_based_policy(cards: str, threshold: int, dealer_card: int, **params)->str:
    """
    100 - threshold chance to take random policy
    threshold change to take max_policy
    """
    randint = random.randint(1, 100)
    if randint < threshold:
        return max_policy(cards, dealer_card=dealer_card, **params)
    return random_policy(cards, **params)
