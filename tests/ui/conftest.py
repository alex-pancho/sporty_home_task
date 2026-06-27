"""
Pytest configuration file.
Defines shared fixtures for browser setup and API client initialization.
"""

import os
import pytest
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test environment configuration
BASE_URL = os.getenv("BASE_URL", "https://qae-assignment-tau.vercel.app")
USER_ID = os.getenv("USER_ID", "test-user-pytest")
API_BASE_URL = os.getenv("API_BASE_URL", BASE_URL + "/api")


@pytest.fixture(scope="session")
def browser_config():
    """Provide browser configuration for all tests."""
    return {
        "base_url": BASE_URL,
        "user_id": USER_ID,
        "api_base_url": API_BASE_URL,
    }


@pytest.fixture(scope="function")
def browser(browser_config):
    """
    Create and yield a Chrome WebDriver instance for each test.
    Automatically handles driver cleanup after test completes.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # Uncomment for headless mode
    # options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    
    # Cleanup
    driver.quit()


@pytest.fixture(scope="function")
def api_client(browser_config):
    """
    Provide an API client with pre-configured headers and base URL.
    Automatically includes x-user-id header for all requests.
    """
    class APIClient:
        def __init__(self, base_url, user_id):
            self.base_url = base_url
            self.headers = {"x-user-id": user_id, "Content-Type": "application/json"}
        
        def get(self, endpoint):
            """GET request."""
            return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        
        def post(self, endpoint, data=None):
            """POST request."""
            return requests.post(
                f"{self.base_url}{endpoint}",
                json=data,
                headers=self.headers
            )
        
        def reset_balance(self):
            """Helper: Reset user balance to initial state."""
            return self.post("/reset-balance")
    
    return APIClient(browser_config["api_base_url"], browser_config["user_id"])