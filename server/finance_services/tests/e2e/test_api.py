import pytest
import requests
from myapi import config

from myapi.adapters.repository import FakeRepository
from myapi.service_layer.unit_of_work import FakeUnitOfWork
from myapi.service_layer import service


def post_to_add_quote(symbol, shortName, longName, displayName, currency, marketCap):
    url = config.get_api_url() + "/add_quote"

    r = requests.post(
        url,
        json={
            "symbol": symbol,
            "shortName": shortName,
            "longName": longName,
            "displayName": displayName,
            "currency": currency,
            "marketCap": marketCap,
        },
    )

    assert r.status_code == 201


@pytest.mark.usefixtures("mysql_db")
@pytest.mark.usefixtures("restart_api")
def test_happy_path_returns_201_and_add_quote(session_factory):
    post_to_add_quote("AAPL", "Apple", "Apple Inc.", "Apple", "USD", 100)
    post_to_add_quote("GOOG", "Alphabet", "Alphabet Inc.", "Alphabet", "USD", 200)


def post_to_add_chart_data(symbol, timestamp, interval, open, high, low, close, volume):
    url = config.get_api_url() + "/add_chart_data"

    r = requests.post(
        url,
        json={
            "symbol": symbol,
            "timestamp": timestamp,
            "interval": interval,
            "open": open,
            "high": high,
            "low": low,
            "close": close,
            "volume": volume,
        },
    )

    assert r.status_code == 201


@pytest.mark.usefixtures("mysql_db")
@pytest.mark.usefixtures("restart_api")
def test_happy_path_returns_201_and_add_chart_data(session_factory):
    post_to_add_chart_data("AAPL", 158888888900, "5m", 10, 20, 5, 15, 100)


def test_happy_path_returns_200_and_get_chart_data(session_factory):
    url = config.get_api_url() + "/get_chart_data"
    r = requests.get(url, params={"symbol": "AAPL", "interval": "5m"})
    assert r.status_code == 200
