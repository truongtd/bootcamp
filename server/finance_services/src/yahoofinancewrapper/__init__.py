import os
import requests

YAHOO_FINANCE_API_KEY = os.environ.get(
    "YAHOO_FINANCE_API_KEY_", "yf8spB0fB23mjw2lIq6VKAcuHd9xW8349q9JSIu3"
)


class APIKeyMissingError(Exception):
    pass


if YAHOO_FINANCE_API_KEY is None:
    raise APIKeyMissingError("YAHOO_FINANCE_API_KEY is missing")

session = requests.Session()
session.headers = {}
session.headers["x-api-key"] = YAHOO_FINANCE_API_KEY

from .yfinquote import YFinQuote
