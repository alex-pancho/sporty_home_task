import pytest
from api.betting_api import BettingApi, PlaceBetRequest


@pytest.mark.api
def test_balance_refresh_returns_actual_balance(betting_api: BettingApi):
    """
    Verify that:
    - a bet can be placed successfully;
    - the user's balance is reduced by the stake amount;
    - all balance-related endpoints return the same value after the transaction.

    This test also detects inconsistencies between `/api/balance`
    and `/api/balance/refresh`.
    """

    before_bet = betting_api.get_balance().balance

    all_matches = betting_api.get_matches()
    first_match = all_matches[0]
    stake = 1
    selection = "HOME"
    body = PlaceBetRequest(match_id=first_match.id, selection=selection, stake=stake)
    place_bet = betting_api.place_bet(body)
    
    assert "successfully" in place_bet.message, (
        f"Expected successful bet placement, got message: '{place_bet.message}'."
    )

    assert place_bet.match_id == first_match.id, (
        f"Expected match_id '{first_match.id}', "
        f"got '{place_bet.match_id}'."
    )

    after_bet_in_response = place_bet.balance
    after_bet = betting_api.get_balance().balance

    assert before_bet > after_bet, (
        f"Balance was not reduced after placing a bet. "
        f"Before: {before_bet}, After: {after_bet}."
    )

    expected_balance = before_bet - stake

    assert after_bet == expected_balance, (
        f"Expected balance to decrease exactly by the stake amount.\n"
        f"Before: {before_bet}\n"
        f"Stake: {stake}\n"
        f"Expected: {expected_balance}\n"
        f"Actual: {after_bet}"
    )

    assert after_bet == after_bet_in_response, (
        f"Balance returned by Place Bet response ({after_bet_in_response}) "
        f"does not match the current balance returned by Balance API ({after_bet})."
    )

    refreshed = betting_api.refresh_balance().balance
    current = betting_api.get_balance().balance

    assert current == refreshed, (
        f"Balance mismatch detected after refresh.\n"
        f"Current balance (/api/balance): {current}\n"
        f"Refreshed balance (/api/balance/refresh): {refreshed}"
    )
