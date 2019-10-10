'''
Created on Oct 10, 2019

@author: maor
'''
from common.cards import count_hand, BjDeck
from common.player import player_standard_logic


def init_game(number_of_players, deck):
    players = []
    for _ in range(number_of_players):
        players.append([deck.deal()])
    dealer = [deck.deal()]
    for player in players:
        player.append(deck.deal())
    return players, dealer


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


def play_hand(cards, dealer, deck):
    count = count_hand(cards)
    while count < 21:
        action = player_standard_logic(cards, dealer)
        if action == 'S':
            break
        elif action == 'D':
            cards.append(deck.deal())
            count = count_hand(cards)
            break
        elif action == 'H':
            cards.append(deck.deal())
            count = count_hand(cards)
        elif action == 'Y':
            # need to split
            # will implement after converting into class
            break

    return count


def play_game(number_of_players, deck, bet):
    # deal first card for everyone:
    players, dealer = init_game(number_of_players, deck)
    final_hand = []
    for player in players:
        final_hand.append(play_hand(player, dealer, deck))
    d_hand = dealer_hand(dealer, deck)
    return final_hand, d_hand, final_money(final_hand, d_hand, bet)


def main():
    b = BjDeck(6)
    play_game(3, b, 100)
    return b


if __name__ == '__main__':
    main()
