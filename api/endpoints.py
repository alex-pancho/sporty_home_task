"""
Autobuilds API endpoint class
"""
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Endpoint:
    """
    Endpoint definition with method, path and optional body.
    """
    method: str
    endpoint: str


@dataclass
class Balance:
    """
    Autobuild class
    """

    @property
    def api_balance_get(self) -> Endpoint:
        """
        Get current balance

        """
        method = "GET"
        endpoint = "/api/balance"
        return Endpoint(method, endpoint)

    @property
    def api_reset_balance_post(self) -> Endpoint:
        """
        Reset balance and return response payload

        """
        method = "POST"
        endpoint = "/api/reset-balance"
        return Endpoint(method, endpoint)


@dataclass
class Bets:
    """
    Autobuild class
    """

    @property
    def api_place_bet_post(self) -> Endpoint:
        """
        Place a bet

        """
        method = "POST"
        endpoint = "/api/place-bet"
        return Endpoint(method, endpoint)

@dataclass
class Matches:
    """
    Autobuild class
    """

    @property
    def api_matches_get(self) -> Endpoint:
        """
        Get all matches

        """
        method = "GET"
        endpoint = "/api/matches"
        return Endpoint(method, endpoint)
