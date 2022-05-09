from flask import Flask, request
from sqlalchemy import Interval

from myapi.domain import model
from myapi.adapters import orm
from myapi.service_layer import service, unit_of_work
import json

app = Flask(__name__)
orm.start_mappers()


@app.route("/add_quote", methods=["POST"])
def add_quote():
    service.add_quote(
        request.json["symbol"],
        request.json["shortName"],
        request.json["longName"],
        request.json["displayName"],
        request.json["currency"],
        request.json["marketCap"],
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return "OK", 201


@app.route("/add_quotes_from_yahoo", methods=["GET"])
def add_quotes_from_yahoo():
    symbols = request.args.getlist("symbols")[0].split(",")
    service.add_quotes_from_yahoo(symbols, unit_of_work.SqlAlchemyUnitOfWork())
    return "OK", 201


@app.route("/get_quotes", methods=["GET"])
def get_quotes():
    symbols = request.args.getlist("symbols")[0].split(",")
    r = service.get_quotes(symbols, unit_of_work.SqlAlchemyUnitOfWork())
    return json.dumps(r), 200


@app.route("/add_chart_data", methods=["POST"])
def add_chart_data():
    service.add_candlestick(
        request.json["symbol"],
        request.json["timestamp"],
        request.json["interval"],
        request.json["open"],
        request.json["high"],
        request.json["low"],
        request.json["close"],
        request.json["volume"],
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return "OK", 201


@app.route("/add_chart_data_from_yahoo", methods=["GET"])
def add_chart_data_from_yahoo():
    symbol = request.args.getlist("symbol")[0]
    service.add_candlesticks_from_yahoo(
        symbol, range_="1mo", uow=unit_of_work.SqlAlchemyUnitOfWork()
    )
    return "OK", 201


@app.route("/get_chart_data", methods=["GET"])
def get_chart_data():
    symbol = request.args.getlist("symbol")[0]
    from_timestamp = request.args.getlist("from")[0]
    to_timestamp = request.args.getlist("to")[0]
    interval = request.args.getlist("interval")[0]
    r = service.get_candlesticks(
        symbol,
        from_timestamp,
        to_timestamp,
        interval,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return json.dumps(r), 200


@app.route("/get_prediction", methods=["GET"])
def get_prediction():
    symbol = request.args.getlist("symbol")[0]
    r = service.get_prediction(symbol, unit_of_work.SqlAlchemyUnitOfWork())
    return json.dumps(r), 200
