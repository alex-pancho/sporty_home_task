from api.client import ApiClient
from api.models import PlaceBetRequest, PlaceBetResponse, Balance, Match
from api.endpoints import Bets, Balance as BalanceEndpoint, Matches


class BettingApi:

    def __init__(self, host: str, user_id: str):
        self.host = host
        self.user_id = user_id

    def get_balance(self) -> Balance:
        client = ApiClient(
            endpoint=BalanceEndpoint().api_balance_get,
            host=self.host,
            schema=Balance,
            headers={"x-user-id": self.user_id},
            validate_response=True,
        )
        return client.request()

    def refresh_balance(self) -> Balance:
        client = ApiClient(
            endpoint=BalanceEndpoint().api_reset_balance_post,
            host=self.host,
            schema=Balance,
            headers={"x-user-id": self.user_id},
            validate_response=True,
        )
        return client.request()

    def get_matches(self) -> list[Match]:
        client = ApiClient(
            endpoint=Matches().api_matches_get,
            host=self.host,
            headers={"x-user-id": self.user_id},
            validate_response=False,
        )

        response = client.request()

        return [Match.model_validate(item) for item in response]

    def place_bet(self, body: PlaceBetRequest) -> PlaceBetResponse:
        client = ApiClient(
            endpoint=Bets().api_place_bet_post,
            host=self.host,
            schema=PlaceBetResponse,
            headers={"x-user-id": self.user_id},
            validate_response=True,
        )
        return client.request(body=body)
