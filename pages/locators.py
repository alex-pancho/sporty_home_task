from dataclasses import dataclass

@dataclass(frozen=True)
class Locator:
    xpath: str
    many: bool = False


class HomePageLocators:

    # Header
    BALANCE_LABEL = '//*[@id="header-balance"]/span[2]'
    
    # Match list & buttons
    HOME_WIN_BUTTONS = Locator('//button[contains(@id,"home")]', many=True)
    DRAW_BUTTONS = Locator('//button[contains(@id,"draw")]', many=True)
    AWAY_WIN_BUTTONS = Locator('//button[contains(@id,"away")]', many=True)

    # Match cards
    ALL_MATCH_CARDS = Locator('//div[@class="card matchCard"]', many=True)
    CARD_BADGES = Locator('//*[@id="match-list"]//span[@class="badge"]', many=True)
    TEAM_NAMES = Locator('//div[@class="teams"]/div[@class="teamRow"]/span[@class="teamName"]', many=True)

    # Bet Slip
    BET_SLIP = '//aside'
    SELECTED_TEAMS = '//div[@class="betSelectionTeams"]'
    SELECTED_MARKET = '//div[@class="betSelectionMarket"]'
    BET_SLIP_BALANCE = '//*[@id="bet-slip-balance"]'
    POTENTIAL_PAYOUT = '//*[@id="bet-slip-potential-payout"]'
    STAKE_INPUT = '//input[@id="bet-slip-stake-input"]'
    PLACE_BET_BUTTON = '//button[@id="bet-slip-place-bet"]'
    REMOVE_ALL_BUTTON = '//button[@id="bet-slip-remove-all"]'
    SELECTED_ODDS = '//span[@class="betSelectionOdds"]'

    # Receipt Modal (Success)
    RECEIPT_MODAL = '//div[@class="card"]/div[@class="modalBody"]'
    RECEIPT_TITLE = '//h2[@class="modalTitle"]'
    BET_ID = '//*[@id="modal-success-bet-id"]'
    RECEIPT_MATCH = '//*[@id="modal-success-match"]'
    RECEIPT_STAKE = '//*[@id="modal-success-stake"]'
    RECEIPT_ODDS = '//*[@id="modal-success-odds"]'
    RECEIPT_PAYOUT = '//*[@id="modal-success-payout"]'
    RECEIPT_TIMESTAMP = '//*[@id="modal-success-placed-at"]'
    RECEIPT_CLOSE_BUTTON = '//*[@id="modal-success-close"]'
    
    # Error Modal
    ERROR_MODAL = '//div[@class="card"]//h2[@class="modalTitle"]'
    ERROR_TEXT = '//*[@id="modal-error-message"]'
    ERROR_REBET_BUTTON = '//button[@id="modal-error-rebet"]'
    ERROR_CLOSE_BUTTON = '//button[@id="modal-error-close"]'
    
    # Validation errors
    STAKE_ERROR = '//*[contains(@class,"error")]'
    INSUFFICIENT_BALANCE_ERROR = '//*[contains(text(),"Insufficient")]'
    MAX_STAKE_ERROR = '//*[contains(text(),"Maximum stake")]'
    MIN_STAKE_ERROR = '//*[contains(text(),"Minimum stake")]'
