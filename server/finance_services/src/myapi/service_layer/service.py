from numpy import iterable
from myapi.domain import model
from myapi.domain.model import Quote, Candlestick
from myapi.service_layer import unit_of_work
import json
import jsonpickle
from yahoofinancewrapper import YFinQuote


class InvalidSymbol(Exception):
    pass


def is_exist(symbol, quotes):
    return symbol in {q.symbol for q in quotes}


def add_quote(
    symbol,
    shortName,
    longName,
    displayName,
    currency,
    marketCap,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        uow.quotes.add_quote(
            model.Quote(symbol, shortName, longName, displayName, currency, marketCap)
        )
        uow.commit()


def get_quotes(symbols: iterable, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        quotes = uow.quotes.get_quotes(symbols)
        encoded = jsonpickle.encode(quotes, unpicklable=False)
        json_data = json.loads(encoded)

        for item in json_data:
            if "_sa_instance_state" in item:
                del item["_sa_instance_state"]
        uow.commit()
    return json_data


# Try to get quotes from yahoo finance and add them to the database
def add_quotes_from_yahoo(symbols: iterable, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        quotes = uow.quotes.get_quotes(symbols)
        for symbol in symbols:
            if not is_exist(symbol, quotes):
                # Try to look up the symbol in yahoo finance

                q = YFinQuote(symbol)
                info = q.real_time_data()

                if info["quoteResponse"]["result"][0]["shortName"] is None:
                    raise InvalidSymbol(f"{symbol} is not a valid symbol")
                else:
                    add_quote(
                        symbol,
                        info["quoteResponse"]["result"][0]["shortName"],
                        info["quoteResponse"]["result"][0]["longName"],
                        info["quoteResponse"]["result"][0]["displayName"],
                        info["quoteResponse"]["result"][0]["currency"],
                        info["quoteResponse"]["result"][0]["marketCap"],
                        uow,
                    )
        uow.commit()


def add_candlestick(
    symbol,
    timestamp,
    interval,
    open,
    high,
    low,
    close,
    volume,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        uow.quotes.add_candlesticks(
            symbol,
            model.Candlestick(
                symbol, timestamp, interval, open, high, low, close, volume
            ),
        )
        uow.commit()


def get_candlesticks(
    symbol, from_timestamp, to_timestamp, interval, uow: unit_of_work.AbstractUnitOfWork
):
    with uow:
        candlesticks = uow.quotes.get_candlesticks(
            symbol, from_timestamp, to_timestamp, interval
        )
        encoded = jsonpickle.encode(candlesticks, unpicklable=False)
        json_data = json.loads(encoded)

        for item in json_data:
            if "_sa_instance_state" in item:
                del item["_sa_instance_state"]

        uow.commit()
    return json_data


def get_candlesticks_from_yahoo(
    symbol,
    range,
    uow: unit_of_work.AbstractUnitOfWork,
):
    quote = uow.quotes.get_quotes(symbol)[0]
    if quote is None:
        raise InvalidSymbol(f"{symbol} is not a valid symbol")
    else:
        q = YFinQuote(symbol)
        data = q.get_chart_data_v2(range=range)
        return data


def add_candlesticks_from_yahoo(
    symbol,
    range_,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        data = get_candlesticks_from_yahoo(symbol=symbol, range=range_, uow=uow)
        for item in data["chart"]["result"]:
            n = len(item["indicators"]["quote"][0]["open"])
            for i in range(n):
                add_candlestick(
                    symbol,
                    item["timestamp"][i],
                    item["meta"]["dataGranularity"],
                    item["indicators"]["quote"][0]["open"][i],
                    item["indicators"]["quote"][0]["high"][i],
                    item["indicators"]["quote"][0]["low"][i],
                    item["indicators"]["quote"][0]["close"][i],
                    item["indicators"]["quote"][0]["volume"][i],
                    uow,
                )
        uow.commit()


def get_prediction(symbol, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        prediction = uow.quotes.get_prediction(symbol)
        encoded = jsonpickle.encode(prediction, unpicklable=False)
        json_data = json.loads(encoded)

        for item in json_data:
            if "_sa_instance_state" in item:
                del item["_sa_instance_state"]
        uow.commit()
    return json_data
