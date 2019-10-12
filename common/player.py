'''
Created on Oct 10, 2019

@author: maor
'''
from common.cards import count_hand
from common.globals import STANDARD_LOGIC


def player_standard_logic(cards, dealer):
    ''' possible outcomes:
        'Y' = split
        'D' = double
        'S' = Stand
        'H' = Hit
    '''
    if dealer[0] == 1:
        dealer_str = 'A'
    else:
        dealer_str = str(dealer[0])
    if len(cards) == 2:
        if cards[0] == cards[1]:
            if cards[0] == 1:
                index = 'A,A'
            else:
                index = f'{cards[0]},{cards[1]}'
        elif cards[0] == 'A':
            index = f'A,{cards[1]}'
        elif cards[1] == 'A':
            index = f'A,{cards[0]}'
        else:
            count = count_hand(cards)
            index = str(count)
    else:
        count = count_hand(cards)
        index = str(count)
    try:
        return STANDARD_LOGIC.loc[index, dealer_str]
    except BaseException:
        print(cards)
