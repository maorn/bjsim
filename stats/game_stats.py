'''
Created on Oct 8, 2019

@author: maor
'''
import pandas as pd
from common.cards import BjDeck, count_hand
from common.game import dealer_hand, play_hand, final_money
from common.player import convert_hand_to_index


def get_percents(old_row):
    row = old_row.copy()
    total = row['win'] + row['lost'] + row['equal']
    row['win'] = row['win'] / total
    row['lost'] = row['lost'] / total
    row['equal'] = row['equal'] / total
    return row


def dealer_stats_for_given_hand(games=1000000, decks=6, save_fn=None):
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
    print(raw_count)
    total = raw_count / raw_count.sum(axis=0)
    print(total)
    if save_fn is not None:
        raw_count.to_csv(save_fn + 'count.csv')
        total.to_csv(save_fn + 'percent.csv')
    return raw_count, total


def player_stats(games=1000000, decks=6, save_fn=None):
    player_stats = {}
    deck = BjDeck(decks)
    for _ in range(games):
        deck.start_game()
        hand = [deck.deal()]
        dealer = [deck.deal()]
        hand.append(deck.deal())
        hand_index = convert_hand_to_index(hand)
        curr_hand = play_hand(hand, dealer, deck, 1)
        for hand in curr_hand:
            if hand.count > 21:
                count = 'F'
            else:
                count = str(hand.count)
            if player_stats.get(hand_index):
                if player_stats[hand_index].get(count):
                    player_stats[hand_index][count] = player_stats[hand_index][count] + 1
                else:
                    player_stats[hand_index][count] = 1
            else:
                player_stats[hand_index] = {}
                player_stats[hand_index][count] = 1

    raw_count = pd.DataFrame(player_stats)
    print(raw_count)
    total = raw_count / raw_count.sum(axis=0)
    print(total)
    if save_fn is not None:
        raw_count.to_csv(save_fn + 'count.csv')
        total.to_csv(save_fn + 'percent.csv')
    return raw_count, total


def player_win_rates_for_start_hands(games=1000000, decks=6, save_fn=None):
    player_stats = {}
    deck = BjDeck(decks)
    for _ in range(games):
        deck.start_game()
        hand = [deck.deal()]
        dealer = [deck.deal()]
        dealer_index = str(dealer[0])
        hand.append(deck.deal())
        hand_index = convert_hand_to_index(hand)
        curr_hand = play_hand(hand, dealer, deck, 1)
        d_cards = dealer_hand(dealer, deck)
        results = final_money(curr_hand, d_cards)
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
            else:
                player_stats[index] = {'win': 0, 'lost': 0, 'equal': 0,
                                       'player_hand': hand_index,
                                       'dealer': dealer_index}
                player_stats[index][end_game] = 1

    raw_count = pd.DataFrame(player_stats)

    total = raw_count.apply(get_percents)
    if save_fn is not None:
        raw_count.to_csv(save_fn + 'count.csv')
        total.to_csv(save_fn + 'percent.csv')
    return raw_count, total


def main():

    raw_count, total = player_win_rates_for_start_hands(10000)
    return raw_count, total


if __name__ == '__main__':
    main()
