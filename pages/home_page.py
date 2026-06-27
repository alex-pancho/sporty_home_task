from pages.locators import HomePageLocators
from pages.base_page import BasePage
from frame.logger import setup_logger

log = setup_logger("home_page")


def get_float_value(cleaned_text:str, strip_text:str):
    cleaned_text = cleaned_text.strip()
    cleaned_text = cleaned_text.replace(strip_text, "")
    try:
        get_float = float(cleaned_text)
    except ValueError:
        log.error("Wrong value: %s", cleaned_text)
        get_float = 0
    return get_float


class HomePage(BasePage, HomePageLocators):

    def __init__(self, driver, base_url, user_id):
        super().__init__(driver)
        self.url = f"{base_url}/?user-id={user_id}"

    def open(self):
        self.driver.get(self.url)

    # ---------- Match selection ----------

    def select_home_win(self, index=0):
        self.item.HOME_WIN_BUTTONS[index].click()

    def select_draw(self, index=0):
        self.item.DRAW_BUTTONS[index].click()

    def select_away_win(self, index=0):
        self.item.AWAY_WIN_BUTTONS[index].click()

    # ---------- Bet Slip ----------

    def enter_stake(self, stake):
        self.item.STAKE_INPUT.send_keys(str(stake))

    def place_bet(self):
        self.item.PLACE_BET_BUTTON.click()

    def remove_all(self):
        self.item.REMOVE_ALL_BUTTON.click()

    # ---------- Getters ----------

    def get_balance(self):
        balance_text = self.item.BALANCE_LABEL.get_text()
        strip_text = "Balance: €"
        balance = get_float_value(balance_text, strip_text)
        return balance

    def get_bet_slip_balance(self):
        balance_text = self.item.BET_SLIP_BALANCE.get_text()
        strip_text = "Balance: €"
        balance = get_float_value(balance_text, strip_text)
        return balance

    def get_selected_teams(self):
        return self.item.TEAMS.get_text()

    def get_selected_market(self):
        return self.item.WINNER.get_text()

    def get_selected_odds(self):
        odds_text = self.item.SELECTED_ODDS.get_text()
        strip_text = "Odds: "
        value = get_float_value(odds_text, strip_text)
        return value

    def get_potential_payout(self):
        payout_text = self.item.POTENTIAL_PAYOUT.get_text()
        strip_text = "€"
        value = get_float_value(payout_text, strip_text)
        return value

    # ---------- Receipt ----------

    def receipt_is_displayed(self):
        return self.item.RECEIPT_MODAL.is_displayed(timeout=5)

    def get_receipt_bet_id(self):
        return self.item.BET_ID.get_text()
    
    def get_receipt_timestamp(self):
        return self.item.RECEIPT_TIMESTAMP.get_text()

    def get_receipt_match(self):
        return self.item.RECEIPT_MATCH.get_text()

    def get_receipt_stake(self):
        stake_text = self.item.RECEIPT_STAKE.get_text()
        strip_text = "€"
        value = get_float_value(stake_text, strip_text)
        return value

    def get_receipt_odds(self):
        odds_value = self.item.RECEIPT_ODDS.get_text()
        value = get_float_value(odds_value, "")
        return value

    def get_receipt_payout(self):
        payout_text = self.item.RECEIPT_PAYOUT.get_text()
        strip_text = "€"
        value = get_float_value(payout_text, strip_text)
        return value

    def close_receipt(self):
        self.item.RECEIPT_CLOSE_BUTTON.click()

    # ---------- Error modal ----------

    def error_modal_is_displayed(self):
        return self.item.ERROR_MODAL.is_displayed()

    def get_error_message(self):
        return self.item.ERROR_TEXT.get_text()

    def click_rebet(self):
        self.item.ERROR_REBET_BUTTON.click()

    def close_error_modal(self):
        self.item.ERROR_CLOSE_BUTTON.click()

    # ---------- Validation ----------

    def stake_error_is_displayed(self):
        return self.item.STAKE_ERROR.is_displayed()

    def insufficient_balance_error_is_displayed(self):
        return self.item.INSUFFICIENT_BALANCE_ERROR.is_displayed()

    def minimum_stake_error_is_displayed(self):
        return self.item.MIN_STAKE_ERROR.is_displayed()

    def maximum_stake_error_is_displayed(self):
        return self.item.MAX_STAKE_ERROR.is_displayed()
