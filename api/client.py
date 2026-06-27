"""
Minimal, robust API client using requests.
"""

from dataclasses import asdict, is_dataclass
from typing import Any, Dict, Optional

import requests
from pydantic import BaseModel, ValidationError
from api.endpoints import Endpoint


class ApiClient:
    """
    Minimal, robust API client using requests.
    """

    @staticmethod
    def check_serialize_body(body: Any) -> Dict[str, Any]:
        """Converted dataclass or dict to dict for API request
        """
        if is_dataclass(body) and not isinstance(body, type):
            return asdict(body)
        return body

    def __init__(
        self,
        endpoint: Endpoint,
        schema: type[BaseModel] | None = None,
        headers: Dict = None,
        timeout: int = 30,
        verify_ssl: bool = True,
        validate_response: bool = False,
    ) -> None:
        """
        endpoint: Endpoint dataclass object
        url = "",
        schema = "",
        headers = "",
        timeout = "",
        verify_ssl = True,
        validate_response = False,
        """
        self.session = requests.Session()
        if headers is not None:
            self.session.headers.update(headers)
        ua_header = {
            "Accept": "application/json",
            "User-Agent": "upc-qa-api-client/1.1",
        }
        self.session.headers.update(ua_header)
        self.url = endpoint.endpoint
        self.method = endpoint.method
        self.params: Dict[str, Any] = {}
        self.data: Dict[str, Any] = {}

        self.schema = schema
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.validate_response = validate_response

    def request(self, body=None) -> Any:
        """
        Docstring for request

        :param self: Description
        :rtype: Any
        """
        if body is not None:
            body = self.check_serialize_body(body)

            if isinstance(body, BaseModel):
                body = body.model_dump(by_alias=True)

            if self.method.lower() == "get":
                self.params = body
            else:
                self.data = body

        try:
            resp = self.session.request(
                method=self.method,
                url=self.url,
                params=self.params,
                json=self.data,
                headers=self.session.headers,
                timeout=self.timeout,
                verify=self.verify_ssl,
            )
        except requests.RequestException as exc:
            raise APIError(-1, str(exc)) from exc

        content_type = resp.headers.get("Content-Type", "")
        body = None
        if resp.text:
            if "application/json" in str(content_type):
                try:
                    body = resp.json()
                except ValueError:
                    body = resp.text
            else:
                body = resp.text or None

        if not resp.ok:
            message = (
                body.get("error") if isinstance(body, dict) else (body or resp.reason)
            )
            raise APIError(resp.status_code, message, response=resp)

        if self.validate_response:
            if self.schema is None:
                raise ValueError("Schema is required")

            return self.validate(body, self.schema)
        return body

    @staticmethod
    def validate(response_json, schema: type[BaseModel]) -> BaseModel:
        """Response pydanic validation"""
        try:
            return schema.model_validate(response_json)
        except ValidationError as e:
            raise AssertionError(f"Schema validation failed:\n{e}") from e


class APIError(Exception):
    """Raised when an API request fails (non-2xx response)."""

    def __init__(
        self,
        status_code: int | None,
        message: str | Any | None,
        response: Optional[requests.Response] = None,
    ):
        super().__init__(f"{status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.response = response
