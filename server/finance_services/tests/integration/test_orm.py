from myapi.domain import model


def test_quote_mapper_can_load_quotes(session):
    session.execute(
        "INSERT INTO Quote (symbol, shortName, longName, displayName, currency, marketCap) VALUES "
        "('AAPL', 'Apple Inc.', 'Apple Inc.', 'Apple', 'USD', 999999999999),"
        "('GRAB', 'Grab Holdings Limited', 'Grab Holdings Limited', 'Grab', 'USD', 13449219072)"
    )

    expected = [
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

    assert session.query(model.Quote).all() == expected


def test_quote_mapper_can_save_quotes(session):
    quote = model.Quote(
        "GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111
    )
    session.add(quote)
    session.commit()

    rows = list(session.execute("SELECT * FROM Quote"))
    assert rows == [
        ("GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111)
    ]


def test_quote_mapper_can_save_candlestick_data(session):
    session.execute(
        "INSERT INTO Quote (symbol, shortName, longName, displayName, currency, marketCap) VALUES "
        "('AAPL', 'Apple Inc.', 'Apple Inc.', 'Apple', 'USD', 999999999999),"
        "('GRAB', 'Grab Holdings Limited', 'Grab Holdings Limited', 'Grab', 'USD', 13449219072)"
    )
    session.commit()

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
    session.add(candlestick)
    session.commit()

    rows = list(session.execute("SELECT * FROM candle_stick"))
    assert rows == [("AAPL", 158888888888, "1m", 1.0, 2.0, 3.0, 4.0, 5)]
