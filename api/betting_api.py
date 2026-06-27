from api.client import ApiClient
from api.models import PlaceBetRequest, PlaceBetResponse, Balance, Match
from api.endpoints import Bets, Balance as BalanceEndpoint, Matches


class BettingApi:

    @staticmethod
    def get_balance() -> Balance:
        client = ApiClient(
            endpoint=BalanceEndpoint().api_balance_get,
            schema=Balance,
            validate_response=True,
        )
        return client.request()

    @staticmethod
    def refresh_balance() -> Balance:
        client = ApiClient(
            endpoint=BalanceEndpoint().api_balance_refresh_get,
            schema=Balance,
            validate_response=True,
        )
        return client.request()

    @staticmethod
    def get_matches() -> list[Match]:
        client = ApiClient(
            endpoint=Matches().api_matches_get,
            validate_response=False,
        )

        response = client.request()

        return [Match.model_validate(item) for item in response]

    @staticmethod
    def place_bet(request: PlaceBetRequest) -> PlaceBetResponse:
        client = ApiClient(
            endpoint=Bets().api_place_bet_post,
            schema=PlaceBetResponse,
            validate_response=True,
        )

        return client.request(request)