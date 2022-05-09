from myapi.adapters.repository import FakeRepository
from myapi.service_layer.unit_of_work import FakeUnitOfWork
from myapi.service_layer import service


def test_add_quote():
    uow = FakeUnitOfWork()
    service.add_quote("AAPL", "Apple Inc.", "Apple Inc.", "NASDAQ", "USD", 100, uow)
    assert uow.quotes.get_quotes(["AAPL"]) is not None
    assert uow.committed


def test_add_quotes_from_yahoo():
    uow = FakeUnitOfWork()
    service.add_quote("AAPL", "Apple Inc.", "Apple Inc.", "NASDAQ", "USD", 100, uow)
    service.add_quotes_from_yahoo(["AAPL", "MSFT"], uow)
    assert uow.quotes.get_quotes(["AAPL", "MSFT"]) is not None
    assert uow.committed


def test_add_candlestick():
    uow = FakeUnitOfWork()
    service.add_quote("AAPL", "Apple Inc.", "Apple Inc.", "NASDAQ", "USD", 100, uow)
    service.add_candlestick("AAPL", "0", "5m", 100, 200, 300, 400, 100000, uow)
    service.add_candlestick("AAPL", "5", "5m", 100, 200, 300, 400, 100000, uow)
    assert uow.quotes.get_candlesticks("AAPL", "0", "999999999999", "5m") is not None
    assert uow.committed


def test_get_candlestick_from_yahoo():
    uow = FakeUnitOfWork()
    service.add_quote("AAPL", "Apple Inc.", "Apple Inc.", "NASDAQ", "USD", 100, uow)
    data = service.get_candlesticks_from_yahoo("AAPL", range="1mo", uow=uow)
    assert data["chart"]["result"][0]["indicators"]["quote"][0]["open"][0] > 0


def test_add_candlesticks_from_yahoo():
    uow = FakeUnitOfWork()
    service.add_quote("AAPL", "Apple Inc.", "Apple Inc.", "NASDAQ", "USD", 100, uow)
    service.add_candlesticks_from_yahoo("AAPL", range_="1mo", uow=uow)
    assert uow.quotes.get_candlesticks("AAPL", "0", "999999999999", "5m") is not None
    assert uow.committed
