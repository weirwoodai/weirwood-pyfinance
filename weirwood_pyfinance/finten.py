import requests
import pandas as pd
import yfinance as yf


class InvalidCredentials(Exception):
    pass


class InvalidQuery(Exception):
    pass


class FinTen:
    def __init__(self):
        self.URI = "https://finten.weirwood.ai"
        self.LOGIN_URI = self.URI + "/users/login"
        self.FILINGS_URI = self.URI + "/company/filings"
        self.MACROS_URI = self.URI + "/fred"
        self._token = None
        self._username = "pyfinance"
        self._password = "pyfinance"

    def _is_reachable(self) -> bool:
        response = requests.get(self.URI)

        if response.status_code == 200:
            try:
                if response.json()["greeting"] == "You reached the FinTen API! 🥳":
                    return True
            except Exception as e:
                print(f"Unable to reach FinTen API {e}")
        return False

    def set_login(self, username, password):
        self._username = username
        self._password = password
        self._token = None

    def _login(self):
        if (self._username == None) or (self._password == None):
            raise InvalidCredentials("username or password has not been set!")

        payload = f"username={self._username}&password={self._password}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(self.LOGIN_URI, headers=headers, data=payload)

        if response.status_code != 200:
            raise InvalidCredentials

        self._token = response.json()["token"]

    def get_filings(self, ticker):
        if self._token == None:
            self._login()

        headers = {"Authorization": f"Bearer {self._token}"}

        response = requests.get(
            self.FILINGS_URI + "?ticker=" + ticker, headers=headers, data={}
        )

        return pd.DataFrame(response.json()["filings"])

    def get_prices(self, ticker, **kwargs):

        df = yf.download(ticker, progress=True, **kwargs)

        if len(df) == 0:
            raise InvalidQuery
        return df

    def list_macros(self):
        if self._token == None:
            self._login()

        headers = {"Authorization": f"Bearer {self._token}"}

        endpoint = self.MACROS_URI + "/names"
        response = requests.get(endpoint, headers=headers, data={})

        return response.json()["names"]

    def get_macro(self, name):
        if self._token == None:
            self._login()

        headers = {"Authorization": f"Bearer {self._token}"}

        endpoint = self.MACROS_URI + "/get"
        response = requests.get(endpoint + "?macro=" + name, headers=headers, data={})
        macro = pd.DataFrame(response.json()["values"]).set_index("date")
        macro.index = pd.to_datetime(macro.index)
        macro.columns = [name]
        return macro
