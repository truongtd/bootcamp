import abc

from numpy import iterable
from myapi.domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_quotes(self, symbols: iterable) -> model.Quote:
        raise NotImplementedError

    @abc.abstractmethod
    def get_candlesticks(
        self,
        symbol: str,
        from_timestamp: int,
        to_timestamp: int,
        interval: str,
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def add_quote(self, quote: model.Quote):
        raise NotImplementedError

    @abc.abstractmethod
    def add_candlesticks(self, candlestick: model.Candlestick):
        raise NotImplementedError

    @abc.abstractmethod
    def get_prediction(self, symbol: str):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def get_quotes(self, symbols):
        if type(symbols) == list:
            quotes = (
                self.session.query(model.Quote)
                .filter(model.Quote.symbol.in_(symbols))
                .all()
            )
        elif type(symbols) == str:
            quotes = (
                self.session.query(model.Quote)
                .filter(model.Quote.symbol == symbols)
                .all()
            )
        return quotes

    def get_candlesticks(
        self,
        symbol: str,
        from_timestamp,
        to_timestamp,
        interval: str,
    ):
        from_timestamp = int(from_timestamp)
        to_timestamp = int(to_timestamp)
        return (
            self.session.query(model.Candlestick)
            .filter(model.Quote.symbol == symbol)
            .filter(model.Candlestick.timestamp >= from_timestamp)
            .filter(model.Candlestick.timestamp <= to_timestamp)
            .filter(model.Candlestick.interval == interval)
            .all()
        )

    def add_quote(self, quote: model.Quote):
        self.session.add(quote)

    def add_candlesticks(self, symbol, candlestick: model.Candlestick):
        self.session.add(candlestick)

    def get_prediction(self, symbol: str):
        return (
            self.session.query(model.Prediction)
            .filter(model.Prediction.symbol == symbol)
            .all()
        )


class FakeRepository(AbstractRepository):
    def __init__(self, quotes):
        self._quotes = set(quotes)

    def get_quotes(self, symbols):
        return [q for q in self._quotes if q.symbol in symbols]

    def add_quote(self, quote):
        self._quotes.add(quote)

    def add_candlesticks(self, symbol, candlestick):
        quote = self.get_quotes([symbol])[0]
        quote.add_candlesticks(candlestick)

    def get_candlesticks(
        self,
        symbol: str,
        from_timestamp,
        to_timestamp,
        interval: str,
    ):
        quote = self.get_quotes([symbol])[0]
        return quote.get_candlesticks(interval, from_timestamp, to_timestamp)

    def get_prediction(self, symbol: str):
        pass
