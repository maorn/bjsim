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


def init_game(number_of_players, deck):
    players = []
    for _ in range(number_of_players):
        players.append([deck.deal()])
    dealer = [deck.deal()]
    for player in players:
        player.append(deck.deal())
    return players, dealer


def player_standard_logic(cards, dealer):
    ''' possible outcomes:
        with two cards:
        'Hit','Double','Stand','Split'
        with more:
        'Hit','Double','Stand'
    '''
    if len(cards) == 2:
        # splits
        if cards[0] == cards[1]:
            # we can split if we want
            if cards[0] == 1:
                return 'Split'
        count = count_hand(cards)

    print(1)


def play_hand(cards, dealer, deck):
    return


def dealer_hand(cards, deck):
    count = count_hand(cards)
    while count < 17:
        cards.append(deck.deal())
        count = count_hand(cards)
    return count


def final_money(final_hands, d_hand, bet):
    ret = []
    for hand in final_hands:
        if hand > 21 or (hand < d_hand and d_hand < 22):
            ret.append(-bet)
        elif d_hand > 21 or hand > d_hand:
            ret.append(bet)
        elif hand == d_hand:
            ret.append(0)
    return ret


def game(number_of_players, deck, bet):
    # deal first card for everyone:
    players, dealer = init_game(number_of_players, deck)
    final_hand = []
    for player in players:
        final_hand.append(play_hand(player, dealer, deck))
    d_hand = dealer_hand(dealer, deck)
    return final_money(final_hand, d_hand, bet)


def main():
    b = BjDeck(6)
    game(3, b)
    return b


if __name__ == '__main__':
    main()
