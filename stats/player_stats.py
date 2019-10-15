'''
Created on 15.10.2019

@author: Darya
'''
import pandas as pd
from common.cards import BjDeck
from common.game import play_hand
from common.player import convert_hand_to_index


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
            if count == '11':
                print(hand.cards, dealer)

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


def main():
    player_stats()


if __name__ == '__main__':
    main()
