'''
Created on Oct 8, 2019

@author: maor
'''
import pandas as pd
from bjsim.common.cards import BjDeck, count_hand
from bjsim.common.game import dealer_hand, play_hand, rewards
from bjsim.common.policies import convert_hand_to_index, fixed_policy
from bjsim.common.globals import WEB_POLICY


def get_percents(old_row: dict) -> dict:
    row = old_row.copy()
    row['win'] = row['win'] / row['total']
    row['lost'] = row['lost'] / row['total']
    row['equal'] = row['equal'] / row['total']
    return row


def dealer_stats_for_given_hand(games: int=1000000, decks: int=6) -> tuple:
    dealer_stats = {}
    for i in range(1, 11):
        dealer_stats[str(i)] = {'17': 0, '18': 0, '19': 0, '20': 0, '21': 0, 'F': 0}
    deck = BjDeck(decks)
    for _ in range(games):
        deck.start_game()
        start_hand = deck.deal()
        dealer = [start_hand]
        d_cards = dealer_hand(dealer, deck)
        count = count_hand(d_cards)
        if count > 21:
            count = 'F'
        dealer_stats[str(start_hand)][str(count)] = dealer_stats[str(start_hand)][str(count)] + 1.
    raw_count = pd.DataFrame(dealer_stats)
    raw_count.index.name = 'end count'
    raw_count.columns.name = 'start hand'
    total = raw_count / raw_count.sum(axis=0)
    return raw_count, total


def fill_stats(hand: list, hand_index: str, p_stats: dict):
    if hand.count > 21:
        count = 'F'
    else:
        count = str(hand.count)
    if p_stats.get(hand_index):
        if p_stats[hand_index].get(count):
            p_stats[hand_index][count] = p_stats[hand_index][count] + 1
        else:
            p_stats[hand_index][count] = 1
    else:
        p_stats[hand_index] = {}
        p_stats[hand_index][count] = 1


def player_stats(games: int=1000000, decks: int=6) -> tuple:
    p_stats = {}
    deck = BjDeck(decks)
    for _ in range(games):
        deck.start_game()
        hand = [deck.deal()]
        dealer = [deck.deal()]
        hand.append(deck.deal())
        hand_index = convert_hand_to_index(hand)
        policy_params = {'dealer_card': dealer[0], 'policy': WEB_POLICY}
        curr_hand = play_hand(hand, dealer[0], deck, 1, fixed_policy, **policy_params)
        for hand in curr_hand:
            fill_stats(hand, hand_index, p_stats)

    raw_count = pd.DataFrame(p_stats)
    raw_count.index.name = 'end count'
    raw_count.columns.name = 'start hand'
    total = raw_count / raw_count.sum(axis=0)
    return raw_count, total


def player_win_rates_for_start_hands(games: int=1000000, decks: int=6) -> tuple:
    player_stats = {}
    deck = BjDeck(decks)
    for _ in range(games):
        deck.start_game()
        hand = [deck.deal()]
        dealer = [deck.deal()]
        dealer_index = str(dealer[0])
        hand.append(deck.deal())
        hand_index = convert_hand_to_index(hand)
        curr_hand = play_hand(hand, dealer[0], deck, 1)
        d_cards = dealer_hand(dealer, deck)
        results = rewards(curr_hand, d_cards)
        for result in results:
            if result > 0:
                end_game = 'win'
            elif result < 0:
                end_game = 'lost'
            else:
                end_game = 'equal'

            index = f'{hand_index}_{dealer_index}'
            if player_stats.get(index):
                player_stats[index][end_game] = player_stats[index][end_game] + 1
                player_stats[index]['total'] = player_stats[index]['total'] + 1
            else:
                player_stats[index] = {'win': 0, 'lost': 0, 'equal': 0, 'total': 1,
                                       'player_hand': hand_index,
                                       'dealer': dealer_index}
                player_stats[index][end_game] = 1

    raw_count = pd.DataFrame(player_stats)
    raw_count.index.name = 'Results'
    raw_count.columns.name = 'Player hand_Dealer hand'
    total = raw_count.apply(get_percents)
    return raw_count, total


def main():

    raw_count, total = player_win_rates_for_start_hands(10000)
    return raw_count, total


if __name__ == '__main__':
    main()
