import pytest
from myapi.domain import model
from myapi.service_layer import unit_of_work


def insert_quote(
    session, symbol, shortName, longName, displayName, currency, marketCap
):
    session.execute(
        "INSERT INTO Quote (symbol, shortName, longName, displayName, currency, marketCap)"
        " VALUES (:symbol, :shortName, :longName, :displayName, :currency, :marketCap)",
        dict(
            symbol=symbol,
            shortName=shortName,
            longName=longName,
            displayName=displayName,
            currency=currency,
            marketCap=marketCap,
        ),
    )


def test_uow_can_retrieve_quotes(session_factory):
    session = session_factory()
    insert_quote(
        session, "AAPL", "Apple Inc.", "Apple Inc.", "Apple", "USD", 999999999999
    )
    insert_quote(
        session,
        "GRAB",
        "Grab Holdings Limited",
        "Grab Holdings Limited",
        "Grab",
        "USD",
        13449219072,
    )
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        quotes = uow.quotes.get_quotes(["AAPL", "GRAB"])
        uow.commit()

    assert len(quotes) == 2


def test_uow_can_add_quotes(session_factory):
    session = session_factory()
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        quote = model.Quote(
            "GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111
        )
        uow.quotes.add_quote(quote)
        uow.commit()

    rows = list(session.execute("SELECT * FROM Quote"))
    assert rows == [
        ("GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111)
    ]


def test_uow_rollback_uncommitted_work_by_default(session_factory):
    session = session_factory()
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        quote = model.Quote(
            "GOOG", "Alphabet Inc.", "Alphabet Inc.", "Alphabet", "USD", 111111111111
        )
        uow.quotes.add_quote(quote)
        # uow.commit()

    rows = list(session.execute("SELECT * FROM Quote"))
    assert rows == []


def test_rollback_on_error(session_factory):
    class MyException(Exception):
        pass

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with pytest.raises(MyException):
        with uow:
            insert_quote(
                uow.session,
                "AAPL",
                "Apple Inc.",
                "Apple Inc.",
                "Apple",
                "USD",
                999999999999,
            )
            raise MyException()

    new_session = session_factory()
    rows = list(new_session.execute("SELECT * FROM Quote"))
    assert rows == []
