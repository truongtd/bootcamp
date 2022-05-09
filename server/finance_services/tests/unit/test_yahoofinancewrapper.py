from yahoofinancewrapper import YFinQuote
from pytest import fixture
import vcr


@fixture
def quote_keys():
    return [
        "language",
        "region",
        "quoteType",
        "typeDisp",
        "quoteSourceName",
        "triggerable",
        "customPriceAlertConfidence",
        "currency",
        "market",
        "esgPopulated",
        "marketState",
        "firstTradeDateMilliseconds",
        "priceHint",
        "preMarketChange",
        "preMarketChangePercent",
        "preMarketTime",
        "preMarketPrice",
        "exchange",
        "shortName",
        "longName",
        "messageBoardId",
        "exchangeTimezoneName",
        "exchangeTimezoneShortName",
        "gmtOffSetMilliseconds",
        "regularMarketChange",
        "regularMarketChangePercent",
        "regularMarketTime",
        "regularMarketPrice",
        "regularMarketDayHigh",
        "regularMarketDayRange",
        "regularMarketDayLow",
        "regularMarketVolume",
        "regularMarketPreviousClose",
        "bid",
        "ask",
        "bidSize",
        "askSize",
        "fullExchangeName",
        "financialCurrency",
        "regularMarketOpen",
        "averageDailyVolume3Month",
        "averageDailyVolume10Day",
        "fiftyTwoWeekLowChange",
        "fiftyTwoWeekLowChangePercent",
        "fiftyTwoWeekRange",
        "fiftyTwoWeekHighChange",
        "fiftyTwoWeekHighChangePercent",
        "fiftyTwoWeekLow",
        "fiftyTwoWeekHigh",
        "dividendDate",
        "earningsTimestamp",
        "earningsTimestampStart",
        "earningsTimestampEnd",
        "trailingAnnualDividendRate",
        "trailingPE",
        "trailingAnnualDividendYield",
        "epsTrailingTwelveMonths",
        "epsForward",
        "epsCurrentYear",
        "priceEpsCurrentYear",
        "sharesOutstanding",
        "bookValue",
        "fiftyDayAverage",
        "fiftyDayAverageChange",
        "fiftyDayAverageChangePercent",
        "twoHundredDayAverage",
        "twoHundredDayAverageChange",
        "twoHundredDayAverageChangePercent",
        "marketCap",
        "forwardPE",
        "priceToBook",
        "sourceInterval",
        "exchangeDataDelayedBy",
        "pageViewGrowthWeekly",
        "averageAnalystRating",
        "tradeable",
        "displayName",
        "symbol",
    ]


def test_quote_init():
    q = YFinQuote("AAPL")
    assert q.symbol == "AAPL"


@vcr.use_cassette(
    "tests/vcr_cassettes/test_quote_info.yaml", filter_headers=["x-api-key"]
)
def test_quote_info(quote_keys):
    q = YFinQuote("AAPL")
    info = q.real_time_data()
    assert info["quoteResponse"]["result"][0]["shortName"] == "Apple Inc."
    assert set(quote_keys).issubset(info["quoteResponse"]["result"][0].keys())


@vcr.use_cassette(
    "tests/vcr_cassettes/test_quote_detailSummary.yaml", filter_headers=["x-api-key"]
)
def test_quote_detail(quote_keys):
    q = YFinQuote("AAPL")
    detail = q.detail()
    assert (
        detail["quoteSummary"]["result"][0]["summaryDetail"]["marketCap"]["raw"]
        > 1000000000000
    )


@vcr.use_cassette(
    "tests/vcr_cassettes/test_chart_data.yaml", filter_headers=["x-api-key"]
)
def test_chart_data():
    q = YFinQuote("AAPL")
    data = q.get_chart_data()
    assert data["id"] == "AAPL"


@vcr.use_cassette(
    "tests/vcr_cassettes/test_chart_data_v2_1mo.yaml", filter_headers=["x-api-key"]
)
def test_chart_data_v2():
    q = YFinQuote("AAPL")
    data = q.get_chart_data_v2(range="1mo")
    assert data["chart"]["result"][0]["indicators"]["quote"][0]["open"][0] > 0
