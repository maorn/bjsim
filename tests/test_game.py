from bjsim.common.cards import BjDeck
from bjsim.common.game import play_hand


def test_game():
    player = [10, 10]
    dealer = [3]
    bet = 50
    deck = BjDeck(6)
    a = play_hand(player, dealer, deck, bet)
