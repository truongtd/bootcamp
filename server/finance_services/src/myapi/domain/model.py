from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass(unsafe_hash=True)
class Candlestick:
    symbol: str
    timestamp: int
    interval: str
    open: float
    high: float
    low: float
    close: float
    volume: int


class Quote:
    def __init__(self, symbol, shortName, longName, displayName, currency, marketCap):
        self.symbol = symbol
        self.shortName = shortName
        self.longName = longName
        self.displayName = displayName
        self.currency = currency
        self.marketCap = marketCap
        self._candlesticks = set()  # type: Set[Candlestick]

    def __repr__(self) -> str:
        return f"<Quote {self.symbol}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Quote):
            return False
        return self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)

    def add_candlesticks(self, candlestick: Candlestick):
        self._candlesticks.add(candlestick)

    def get_candlesticks(self, interval: str, from_timestamp, to_timestamp):
        from_timestamp = int(from_timestamp)
        to_timestamp = int(to_timestamp)
        return [
            c
            for c in self._candlesticks
            if c.interval == interval
            and int(c.timestamp) >= from_timestamp
            and int(c.timestamp) <= to_timestamp
        ]


@dataclass(unsafe_hash=True)
class Prediction:
    id: int
    date: date
    symbol: str
    predicted_value: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
