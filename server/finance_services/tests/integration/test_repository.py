from myapi.domain import model
from myapi.adapters import repository
import pytest


def test_repository_can_retrieve_quotes(session):
    session.execute(
        "INSERT INTO Quote (symbol, shortName, longName, displayName, currency, marketCap) VALUES "
        "('AAPL', 'Apple Inc.', 'Apple Inc.', 'Apple', 'USD', 999999999999),"
        "('GRAB', 'Grab Holdings Limited', 'Grab Holdings Limited', 'Grab', 'USD', 13449219072)"
    )

    repo = repository.SQLAlchemyRepository(session)
    retrieved = repo.get_quotes(["AAPL", "GRAB"])

    assert retrieved == [
        model.Quote("AAPL", "Apple Inc.", "Apple Inc.", "Apple", "USD", 999999999999),
        model.Quote(
            "GRAB",
            "Grab Holdings Limited",
            "Grab Holdings Limited",
            "Grab",
            "USD",
            13449219072,
        ),
    ]


def test_repository_can_save_a_quote(session):
    quote = model.Quote(
        "GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111
    )
    repo = repository.SQLAlchemyRepository(session)
    repo.add_quote(quote)
    session.commit()

    rows = list(session.execute("SELECT * FROM Quote"))

    assert rows == [
        ("GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111)
    ]


def test_repository_can_save_candlestick_data(session):
    session.execute(
        "INSERT INTO Quote (symbol, shortName, longName, displayName, currency, marketCap) VALUES "
        "('AAPL', 'Apple Inc.', 'Apple Inc.', 'Apple', 'USD', 999999999999),"
        "('GRAB', 'Grab Holdings Limited', 'Grab Holdings Limited', 'Grab', 'USD', 13449219072)"
    )

    candlestick = model.Candlestick(
        "AAPL",
        158888888888,
        "1m",
        1.0,
        2.0,
        3.0,
        4.0,
        5,
    )
    repo = repository.SQLAlchemyRepository(session)
    repo.add_candlesticks("AAPL", candlestick)
    session.commit()

    rows = list(session.execute("SELECT * FROM candle_stick"))

    assert rows == [("AAPL", 158888888888, "1m", 1.0, 2.0, 3.0, 4.0, 5)]


def test_repository_can_retrieve_candlestick_data(session):
    session.execute(
        "INSERT INTO Quote (symbol, shortName, longName, displayName, currency, marketCap) VALUES "
        "('AAPL', 'Apple Inc.', 'Apple Inc.', 'Apple', 'USD', 999999999999),"
        "('GRAB', 'Grab Holdings Limited', 'Grab Holdings Limited', 'Grab', 'USD', 13449219072)"
    )

    session.commit()

    session.execute(
        "INSERT INTO candle_stick (symbol, timestamp, interval, open, high, low, close, volume) VALUES "
        "('AAPL', 158888888888, '1m', 1.0, 2.0, 3.0, 4.0, 5)"
    )

    session.commit()

    repo = repository.SQLAlchemyRepository(session)
    retrieved = repo.get_candlesticks("AAPL", 158888888800, 158888888890, "1m")

    assert len(retrieved) == 1
