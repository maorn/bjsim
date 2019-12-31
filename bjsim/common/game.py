'''
Created on Oct 10, 2019

@author: maor
'''
from bjsim.common.cards import count_hand, BjDeck
from bjsim.common.policies import policy_selector


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
    def __init__(self, cards: list, bet: float, dealer: int, action: str):
        self.bet = bet
        self.cards = cards.copy()
        self.count = count_hand(cards)
        self.actions = [{'hand': self.cards.copy(), 'dealer': dealer, 'action': action}]
        self.reward = 0

    def hit(self, deck: BjDeck):
        self.cards.append(deck.deal())
        self.count = count_hand(self.cards)

    def add_action(self, dealer: int, action: str, cards: list=None):
        if cards:
            self.actions.append({'hand': cards.copy(), 'dealer': dealer, 'action': action})
        else:
            self.actions.append({'hand': self.cards.copy(), 'dealer': dealer, 'action': action})


def init_game(number_of_players: int, deck: BjDeck) -> tuple:
    players = []
    for _ in range(number_of_players):
        players.append([deck.deal()])
    dealer = [deck.deal()]
    for player in players:
        player.append(deck.deal())
    return players, dealer


def dealer_hand(cards: list, deck: BjDeck) -> list:
    count = count_hand(cards)
    while count < 17:
        cards.append(deck.deal())
        count = count_hand(cards)
    return cards


def rewards(final_hands: list, d_cards: list) -> list:
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
                hand.reward = -hand.bet
            # player has blackjack in two cards and dealer don't have 21 in two cards
            elif hand.count == 21 and len(hand.cards) == 2 and (d_hand != 21 or len(d_cards) > 2):
                ret.append(hand.bet * 1.5)
                hand.reward = hand.bet * 1.5
            # dealer has more than 21 or the player has more than the dealer
            elif d_hand > 21 or hand.count > d_hand:
                ret.append(hand.bet)
                hand.reward = hand.bet

            # same hand for dealer and player
            elif hand.count == d_hand:
                ret.append(0)
                hand.reward = 0
            else:
                print(1)
        return ret
    except BaseException:
        print(1)


def play_double(hand: list, bet: float,
                deck: BjDeck, dealer: int) -> OneHand:
    curr_hand = OneHand(hand, bet * 2, dealer, 'D')
    curr_hand.hit(deck)
    return curr_hand


def play_hit(hand: list, bet: float, dealer: int,
             deck: BjDeck, policy_func, **policy_params) -> OneHand:
    curr_hand = OneHand(hand, bet, dealer, 'H')
    action = policy_selector(policy_func, cards=curr_hand.cards, **policy_params)
    while action != 'S':
        curr_hand.hit(deck)
        if curr_hand.count > 21:
            break
        else:
            action = policy_selector(policy_func, cards=curr_hand.cards, **policy_params)
            curr_hand.add_action(dealer, action)
    return curr_hand


def add_split_action(cur_hand: int, dealer: int):
    cur_hand.add_action(dealer, 'Y', [cur_hand.cards[0], cur_hand.cards[0]])


def play_split(hand: list, bet: int, dealer: int, deck: BjDeck, policy_func, **policy_params):
    final_hand = []
    # ace means split and one card only.
    if hand[0] == 1:

        for _ in range(2):
            cur_hand = OneHand([hand.pop(), deck.deal()], bet, dealer, 'Y')
            cur_hand.actions = [{'hand': [1, 1], 'dealer': dealer, 'action': 'Y'}]
            final_hand.append(cur_hand)
        return final_hand
    while hand:
        curr_hand = [hand.pop(), deck.deal()]
        action = policy_selector(policy_func, cards=curr_hand, **policy_params)
        if action == 'S':
            cur_hand = OneHand(curr_hand, bet, dealer, action)
            add_split_action(cur_hand, dealer)
            final_hand.append(cur_hand)
        elif action == 'D':
            hand_d = play_double(curr_hand, bet, deck, dealer)
            add_split_action(hand_d, dealer)
            final_hand.append(hand_d)
        elif action == 'Y':
            hand.append(curr_hand.pop())
            hand.append(curr_hand.pop())
        elif action == 'H':
            hand_h = play_hit(curr_hand, bet, dealer, deck, policy_func, **policy_params)
            add_split_action(hand_h, dealer)
            final_hand.append(hand_h)
        else:
            print("action not understood ", action)
    return final_hand


def play_hand(hand: list, dealer: int, deck: BjDeck,
              bet: float, policy_func, **policy_params) -> tuple:
    action = policy_selector(policy_func, cards=hand, **policy_params)
    if action == 'S':
        curr_hand = OneHand(hand, bet, dealer, action)
        return [curr_hand]
    if action == 'D':
        return [play_double(hand, bet, deck, dealer)]
    if action == 'H':
        return [play_hit(hand, bet, dealer, deck, policy_func, **policy_params)]

    if action == 'Y':
        return play_split(hand, bet, dealer, deck, policy_func, **policy_params)
    print("no action to perform")
    raise


def play_game(deck, bets, policy_func, **policy_params):
    # deal first card for everyone:
    players, dealer = init_game(len(bets), deck)
    policy_params['dealer_card'] = dealer[0]
    final_hand = []

    for player, bet in zip(players, bets):
        curr_hand = play_hand(player, dealer[0], deck, bet, policy_func, **policy_params)
        final_hand.extend(curr_hand)
    d_hand = dealer_hand(dealer, deck)
    return final_hand, d_hand, rewards(final_hand, d_hand)


def main():
    b = BjDeck(6)
    start_money = 0
    end_money = start_money
    games = 10000
    for i in range(games):
        print(i)
        b.start_game()
        final_hand, d_hand, return_money = play_game(b, [100, 100, 100, 100, 100, 100])
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
