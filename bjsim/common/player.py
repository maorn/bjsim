'''
Created on Oct 10, 2019

@author: maor
'''
import pandas as pd
from bjsim.common.cards import count_hand


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


def player_policy(cards: list, dealer: int, policy: pd.DataFrame) -> str:

    if dealer == 1:
        dealer_str = 'A'
    else:
        dealer_str = str(dealer)
    index = convert_hand_to_index(cards)
    try:
        pol = policy.loc[index, dealer_str]
        if len(cards) > 2 and pol == 'D':
            return 'H'
        return pol
    except BaseException:
        print(cards)
