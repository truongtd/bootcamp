from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    BigInteger,
    String,
    Date,
    Float,
    ForeignKey,
)
from sqlalchemy.orm import mapper, relationship
from myapi.domain import model

metadata = MetaData()

quote = Table(
    "quote",
    metadata,
    Column("symbol", String(10), primary_key=True),
    Column("shortName", String(100)),
    Column("longName", String(255)),
    Column("displayName", String(100)),
    Column("currency", String(10)),
    Column("marketCap", BigInteger),
)

candle_stick = Table(
    "candle_stick",
    metadata,
    Column(
        "symbol",
        String(10),
        ForeignKey("quote.symbol"),
        primary_key=True,
    ),
    Column("timestamp", BigInteger, primary_key=True),
    Column("interval", String(10), primary_key=True),
    Column("open", Float),
    Column("high", Float),
    Column("low", Float),
    Column("close", Float),
    Column("volume", Integer),
)

prediction = Table(
    "stock_prediction",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("date", Date),
    Column("symbol", String(10)),
    Column("predicted_value", String(45)),
    Column("created_at", Date),
    Column("updated_at", Date),
)


def start_mappers():
    quote_mapper = mapper(model.Quote, quote)

    mapper(
        model.Candlestick,
        candle_stick,
        properties={"quote": relationship(quote_mapper)},
    )

    mapper(model.Prediction, prediction)
