from bjsim.common.cards import BjDeck
from bjsim.common.game import play_hand
from bjsim.common.policies import fixed_policy
from bjsim.common.globals import WEB_POLICY


def test_game():
    player = [10, 10]
    dealer = [3]
    bet = 50
    deck = BjDeck(6)
    policy_params = {'dealer_card': dealer[0], 'policy': WEB_POLICY}
    a = play_hand(player, dealer[0], deck, bet, fixed_policy, **policy_params)
