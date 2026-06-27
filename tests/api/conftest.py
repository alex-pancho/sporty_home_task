import pytest
import os

from dotenv import load_dotenv
from api.betting_api import BettingApi

load_dotenv()


@pytest.fixture(scope="session")
def host() -> str:
    return os.environ["BASE_URL"].rstrip("/")


@pytest.fixture(scope="session")
def user_id() -> str:
    return os.environ["USER_ID"]


@pytest.fixture(scope="session")
def betting_api(host, user_id):
    betting = BettingApi(host, user_id)
    return betting
