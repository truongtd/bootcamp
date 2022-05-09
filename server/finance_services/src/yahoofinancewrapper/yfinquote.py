from . import session


class YFinQuote(object):
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def real_time_data(self):
        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols": f"{self.symbol}"}
        response = session.get(url=url, params=querystring)
        return response.json()

    def detail(self, modules="summaryDetail"):
        url = f"https://yfapi.net/v11/finance/quoteSummary/{self.symbol}"
        querystring = {"modules": f"{modules}"}
        response = session.get(url=url, params=querystring)
        return response.json()

    def get_chart_data(self, period="1Y"):
        url = f"https://alpha.financeapi.net/symbol/get-chart"
        querystring = {"period": f"{period}", "symbol": f"{self.symbol}"}
        response = session.get(url=url, params=querystring)
        return response.json()

    def get_chart_data_v2(self, region="US", range="max", interval="5m"):
        url = f"https://yfapi.net/v8/finance/chart/{self.symbol}"
        querystring = {
            "region": f"{region}",
            "range": f"{range}",
            "interval": f"{interval}",
        }
        response = session.get(url=url, params=querystring)
        return response.json()
