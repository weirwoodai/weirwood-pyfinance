import os

import pytest
from dotenv import load_dotenv

from weirwood_pyfinance import FinTen
from weirwood_pyfinance.finten import InvalidCredentials, InvalidQuery

load_dotenv()

USER = os.environ["PYFINANCE_USERNAME"]
PASSWORD = os.environ["PYFINANCE_USERNAME"]


def test_is_reachable():
    finten = FinTen()
    assert finten._is_reachable()
    finten.URI = "https://www.google.com"
    assert finten._is_reachable() is False


def test_login__invalid_credentials():
    with pytest.raises(InvalidCredentials):
        finten = FinTen()
        finten.set_login(username="foo", password="bar")
        finten._login()


def test_login():
    finten = FinTen()
    finten.set_login(username=USER, password=PASSWORD)
    finten._login()


def test_get_filings():
    finten = FinTen()
    finten.set_login(username=USER, password=PASSWORD)

    filings = finten.get_filings(ticker="AAPL")
    assert len(filings) > 0
    filings = FinTen().get_filings(ticker="AAPL")
    assert len(filings) > 0


def test_get_prices():
    aapl = FinTen().get_prices(ticker="AAPL")
    assert len(aapl) > 0


def test_get_prices_last_year():
    aapl = FinTen().get_prices(ticker="AAPL", start="2019-01-01", end="2020-01-01")
    assert len(aapl) == 253


def test_unknown_ticker():
    with pytest.raises(InvalidQuery):
        FinTen().get_prices(ticker="asdf")


def test_get_macros():
    finten = FinTen()
    finten.set_login(username=USER, password=PASSWORD)
    available_macros = finten.list_macros()
    assert available_macros == ["DGORDER", "ACDGNO", "DMOTRC1Q027SBEA", "IPDCONGD"]

    dgorder = finten.get_macro(name="DGORDER")
    acdgno = finten.get_macro(name="ACDGNO")

    assert dgorder.iloc[0].values[0] == 114535
    assert acdgno.iloc[0].values[0] == 19863


def test_get_tickers():
    finten = FinTen()
    finten.set_login(username=USER, password=PASSWORD)
    all_tickers = finten.get_tickers()
    assert len(all_tickers) == 9434
