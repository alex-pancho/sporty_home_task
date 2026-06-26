from base_page import BasePage


class HomePageLocator(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Header
    balance_label = '//*[@id="header-balance"]/span[2]'

    # Navigation / Buttons
    place_bet_button = '//button[.="Place Bet"]'
    close_receipt_button = '//button[.="Close"]'

    # Match cards
    all_match_cards = '//div[@class="card matchCard"]'
    card_badges = '//*[@id="match-list"]//span[@class="badge"]'
    team_names = '//div[@class="teams"]/div[@class="teamRow"]/span[@class="teamName"]'
    home_win_buttons = '//button[contains(@id,"home")]'
    draw_buttons = '//button[contains(@id,"draw")]'
    away_win_buttons = '//button[contains(@id,"away")]'

    # Bet Slip
    bet_slip = '//aside'
    bet_slip_balance = '//*[@id="bet-slip-balance"]'
    teams = '//div[@class="betSelectionTeams"]'
    winner = '//div[@class="betSelectionMarket"]'
    selected_odds = '//span[@class="betSelectionOdds"]'
    stake_input = '//input[@id="bet-slip-stake-input"]'
    potential_payout = '//*[@id="bet-slip-potential-payout"]'

    # Receipt Modal
    receipt_modal = '//div[@class="card"]/div[@class="modalBody"]'
    receipt_title = '//h2[@class="modalTitle"]'
    bet_id = '//*[@id="modal-success-bet-id"]'
    receipt_match = '//*[@id="modal-success-match"]'
    receipt_stake = '//*[@id="modal-success-stake"]'
    receipt_odds = '//*[@id="modal-success-odds"]'
    receipt_payout = '//*[@id="modal-success-payout"]'
    receipt_timestamp = '//*[@id="modal-success-placed-at"]'
    receipt_close_button = '//*[@id="modal-success-close"]'

    # Validation
    stake_error = '//*[contains(@class,"error")]'
    insufficient_balance_error = '//*[contains(text(),"Insufficient")]'
