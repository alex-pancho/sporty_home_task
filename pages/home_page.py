from locators import HomePageLocators
from base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver, base_url, user_id):
        super().__init__(driver)
        self.main_page_url = f"{base_url}/?user-id={user_id}"
    
    def open(self):
        self.driver.get(self.url)

    # ---------- Match selection ----------

    def select_home_win(self, index=0):
        self.find_elements(By.XPATH, HomePageLocators.HOME_WIN_BUTTONS)[index].click()

    def select_draw(self, index=0):
        self.find_elements(By.XPATH, HomePageLocators.DRAW_BUTTONS)[index].click()

    def select_away_win(self, index=0):
        self.find_elements(By.XPATH, HomePageLocators.AWAY_WIN_BUTTONS)[index].click()

    # ---------- Bet Slip ----------

    def enter_stake(self, stake):
        field = self.find(By.XPATH, HomePageLocators.STAKE_INPUT)
        field.clear()
        field.send_keys(str(stake))

    def place_bet(self):
        self.find(By.XPATH, HomePageLocators.PLACE_BET_BUTTON).click()

    # ---------- Getters ----------

    def get_balance(self):
        return self.find(By.XPATH, HomePageLocators.BALANCE).text

    def get_payout(self):
        return self.find(By.XPATH, HomePageLocators.POTENTIAL_PAYOUT).text

    def get_selected_odds(self):
        return self.find(By.XPATH, HomePageLocators.SELECTED_ODDS).text

    # ---------- Receipt ----------

    def receipt_is_displayed(self):
        return self.find(By.XPATH, HomePageLocators.RECEIPT_MODAL).is_displayed()

    def get_receipt_bet_id(self):
        return self.find(By.XPATH, HomePageLocators.BET_ID).text

    def close_receipt(self):
        self.find(By.XPATH, HomePageLocators.RECEIPT_CLOSE_BUTTON).click()

    # ---------- Validation ----------

    def stake_error_is_displayed(self):
        return self.find(By.XPATH, HomePageLocators.STAKE_ERROR).is_displayed()

    def insufficient_balance_error_is_displayed(self):
        return self.find(By.XPATH, HomePageLocators.INSUFFICIENT_BALANCE_ERROR).is_displayed()


if __name__ == "__main__":
    driver = ""
    my_home = HomePage(driver)
    item = my_home.item.menu_home
    print(item)
