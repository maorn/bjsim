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
    return cards


def final_money(final_hands, d_cards):
    try:
        ret = []
        d_hand = count_hand(d_cards)
        for hand in final_hands:
            # player has over 21  or
            # player has less than the dealer or
            # dealer has 21 in two cards and the player don't have 21 in two cards
            if (hand.count > 21 or (hand.count < d_hand and d_hand < 22)) or (
                    d_hand == 21 and len(d_cards) == 2 and len(hand.cards) > 2):
                ret.append(-hand.bet)
            # player has blackjack in two cards and dealer don't have 21 in two cards
            elif hand.count == 21 and len(hand.cards) == 2 and (d_hand != 21 or len(d_cards) > 2):
                ret.append(hand.bet * 1.5)
            # dealer has more than 21 or the player has more than the dealer
            elif d_hand > 21 or hand.count > d_hand:
                ret.append(hand.bet)
            # same hand for dealer and player
            elif hand.count == d_hand:
                ret.append(0)
            else:
                print(1)
        return ret
    except BaseException:
        print(1)


def play_double(hand, bet, deck):
    curr_hand = OneHand(hand, bet * 2)
    curr_hand.hit(deck)
    return curr_hand


def play_hit(hand, bet, dealer, deck):
    curr_hand = OneHand(hand, bet)
    action = player_standard_logic(curr_hand.cards, dealer)
    while action != 'S':
        curr_hand.hit(deck)
        if curr_hand.count > 21:
            break
        else:
            action = player_standard_logic(curr_hand.cards, dealer)
    return curr_hand


def play_hand(hand, dealer, deck, bet):
    action = player_standard_logic(hand, dealer)
    if action == 'S':
        curr_hand = OneHand(hand, bet)
        return [curr_hand]
    if action == 'D':
        return [play_double(hand, bet, deck)]
    if action == 'H':
        return [play_hit(hand, bet, dealer, deck)]

    if action == 'Y':
        final_hand = []
        # ace means split and one card only.
        if hand[0] == 1:
            first_h = OneHand([hand.pop(), deck.deal()], bet)
            final_hand.append(first_h)
            second_h = OneHand([hand.pop(), deck.deal()], bet)
            final_hand.append(second_h)
            return final_hand
        while hand:
            curr_hand = [hand.pop(), deck.deal()]
            action = player_standard_logic(curr_hand, dealer)
            if action == 'S':
                final_hand.append(OneHand(curr_hand, bet))
            elif action == 'D':
                final_hand.append(play_double(curr_hand, bet, deck))
            elif action == 'Y':
                hand.append(curr_hand.pop())
                hand.append(curr_hand.pop())
            elif action == 'H':
                final_hand.append(play_hit(curr_hand, bet, dealer, deck))
            else:
                print("action not understood ", action)
        return final_hand


def play_game(deck, bets):
    # deal first card for everyone:
    players, dealer = init_game(len(bets), deck)
    final_hand = []
    for player, bet in zip(players, bets):
        curr_hand = play_hand(player, dealer, deck, bet)
        final_hand.extend(curr_hand)
    d_hand = dealer_hand(dealer, deck)
    return final_hand, d_hand, final_money(final_hand, d_hand)


class PlayerHand:

    def __init__(self, cards, bet):
        self.hands = [OneHand(cards, bet)]
        self.total_bet = bet

    def split_hand(self, hand_index, deck):
        split_card = self.hands[hand_index].cards.pop()
        bet = self.hands[hand_index].bet
        self.hands[hand_index].cards.append(deck.deal())
        new_hand = OneHand([split_card], bet)
        new_hand.cards.append(deck.deal())
        self.hands.append(new_hand)
        self.total_bet = self.total_bet + bet

    def double(self, hand_index, deck):
        bet = self.hands[hand_index].bet
        self.total_bet = self.total_bet + bet
        self.hands[hand_index].cards.append(deck.deal())
        self.hands[hand_index].bet = bet + bet


class OneHand:
    def __init__(self, cards, bet):
        self.bet = bet
        self.cards = cards
        self.count = count_hand(cards)

    def hit(self, deck: BjDeck):
        self.cards.append(deck.deal())
        self.count = count_hand(self.cards)


def main():
    b = BjDeck(6)
    start_money = 10000
    end_money = start_money
    games = 1000
    for i in range(games):
        print(i)
        b.start_game()
        final_hand, d_hand, return_money = play_game(b, [100, 100, 100])
        if final_hand is None or return_money is None:
            print(2)
        if len(final_hand) < 3 or len(return_money) < 3:
            print(1)
        for hand in final_hand:
            print(hand.cards)
        print("dealer", d_hand)
        print(return_money)
        end_money = end_money + sum(return_money)
        print("money", end_money)
    print(end_money)
    print("average win/lost per game: ", (end_money - start_money) / games)


if __name__ == '__main__':
    main()
