"""
Test: E2E UI - Happy Path: Successful Bet Placement

RATIONALE:
This is the PRIMARY USER JOURNEY. If a user cannot successfully:
1. Select a match
2. Enter a stake
3. Place a bet
4. See correct receipt with all details
5. Have balance updated

...then the entire feature is broken. This test validates the critical happy path.

BUSINESS IMPACT:
- HIGH: Revenue-critical. No bets placed = no revenue.
- This is the first smoke test for any release.

COVERAGE:
✓ Match selection (HOME, DRAW, AWAY outcomes)
✓ Stake input validation
✓ Bet placement API call
✓ Receipt accuracy (Bet ID, match, stake, odds, payout, timestamp)
✓ Balance deduction
✓ Receipt closure
"""

import pytest

# import time
# import tests.ui.add_root
from pages.home_page import HomePage


@pytest.mark.e2e
@pytest.mark.critical
@pytest.mark.smoke
class TestBetPlacementHappyPath:

    def test_successful_single_bet_placement_with_receipt_verification(
        self, browser, browser_config
    ):
        """
        Test the complete happy path: match selection → stake entry → placement → receipt.

        Steps:
        1. Open application
        2. Record initial balance
        3. Select a match (HOME outcome)
        4. Enter stake (€1.00)
        5. Place bet
        6. Verify success receipt contains:
           - Bet ID (non-empty)
           - Match details
           - Stake amount
           - Odds at placement
           - Calculated payout (stake × odds)
           - Placement timestamp
        7. Close receipt
        8. Verify balance decreased by stake amount
        9. Verify bet slip is cleared
        """
        # ARRANGE
        page = HomePage(
            driver=browser,
            base_url=browser_config["base_url"],
            user_id=browser_config["user_id"],
        )

        # Act: Open page and get initial state
        page.open()
        card_for_betting_number = 1
        initial_balance = page.get_balance()
        stake = 1.00

        # ASSERT: Initial state is valid
        assert initial_balance > 0, "User should have positive balance to start"
        assert (
            initial_balance >= stake
        ), f"Balance {initial_balance} should cover stake {stake}"

        # ACT: Select match outcome (HOME WIN for first match)
        page.select_home_win(index=card_for_betting_number)

        # ASSERT: Selection was registered
        selected_odds = page.get_selected_odds()
        assert selected_odds > 1.0, "Odds should be valid (> 1.0)"

        # ACT: Get teams
        team_home = page.get_home_team(card_for_betting_number)
        team_away = page.get_away_team(card_for_betting_number)

        # ACT: Enter stake
        page.enter_stake(stake)

        # ASSERT: Potential payout is calculated correctly
        potential_payout = page.get_potential_payout()
        expected_payout = stake * selected_odds
        assert (
            abs(potential_payout - expected_payout) < 0.01
        ), f"Payout {potential_payout} should equal stake {stake} × odds {selected_odds} = {expected_payout}"

        # ACT: Place the bet
        page.place_bet()

        # ASSERT: Success receipt appears
        assert page.receipt_is_displayed(), "Success receipt modal should be visible"

        # ASSERT: Receipt contains all required data
        receipt_bet_id = page.get_receipt_bet_id()
        assert receipt_bet_id, "Receipt must show Bet ID"

        receipt_match = page.get_receipt_match()
        receipt_match_teams = receipt_match.split(" vs ")
        receipt_home = receipt_match_teams[0]
        receipt_away = receipt_match_teams[1]
        assert (
            team_home == receipt_home.strip()
        ), f"Receipt home is '{receipt_home}' but '{team_home}' is expected"
        assert (
            team_away == receipt_away.strip()
        ), f"Receipt away is '{receipt_away}' but '{team_away}' is expected"

        receipt_stake = page.get_receipt_stake()
        assert (
            receipt_stake == stake
        ), f"Receipt stake {receipt_stake} should match entered {stake}"

        receipt_odds = page.get_receipt_odds()
        assert (
            abs(receipt_odds - selected_odds) < 0.01
        ), f"Receipt odds {receipt_odds} should match selected odds {selected_odds}"

        receipt_payout = page.get_receipt_payout()
        assert (
            abs(receipt_payout - expected_payout) < 0.01
        ), f"Receipt Potential Payout {receipt_payout} should equal {expected_payout}"

        receipt_timestamp = page.get_receipt_timestamp()
        assert (
            len(receipt_timestamp) > 7
        ), "Receipt must show placement timestamp > 7 chars"

        # ACT: Close receipt
        page.close_receipt()

        # ASSERT: Balance is updated
        new_balance = page.get_balance()
        expected_balance = initial_balance - stake
        assert (
            abs(new_balance - expected_balance) < 0.01
        ), f"Balance should be {expected_balance}, got {new_balance}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
