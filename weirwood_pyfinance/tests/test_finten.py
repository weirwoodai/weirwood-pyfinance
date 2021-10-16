import pytest
from weirwood_pyfinance.finten import FinTen, InvalidCredentials, InvalidQuery
import json
import httpretty


@pytest.fixture
def finten_login():
    with open("./.credentials.json") as f:
        finten_login = json.load(f)
    return finten_login


def test_is_reachable():
    finten = FinTen()
    assert finten._is_reachable()
    finten.URI = "https://www.google.com"
    assert finten._is_reachable() == False


def test_login__invalid_credentials():
    with pytest.raises(InvalidCredentials):
        finten = FinTen()
        finten.set_login(username="foo", password="bar")
        finten._login()


def test_login(finten_login):
    finten = FinTen()
    finten.set_login(**finten_login)
    finten._login()


def test_get_filings(finten_login):
    finten = FinTen()
    finten.set_login(**finten_login)
    filings = finten.get_filings(ticker="AAPL")
    assert len(filings) > 0


def test_get_filings_with_public_login():
    # httpretty.enable()
    # httpretty.register_uri(
    #     httpretty.GET,
    #     "https://finten.weirwood.ai/company/filings?ticker=AAPL",
    #     body='{"filings": [{"foo": "bar", "manchu": "massachusets"}]}',
    # )
    # httpretty.register_uri(
    #     httpretty.POST,
    #     "https://finten.weirwood.ai/users/login",
    #     body='{"token": "test"}',
    # )

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

def test_get_macros(finten_login):
    finten = FinTen()
    finten.set_login(**finten_login)
    available_macros = finten.list_macros()
    assert available_macros == ["DGORDER", "ACDGNO", "DMOTRC1Q027SBEA", "IPDCONGD"]

    dgorder = finten.get_macro(name="DGORDER")
    acdgno = finten.get_macro(name="ACDGNO")

    assert dgorder.iloc[0].values[0] == 114535
    assert acdgno.iloc[0].values[0] == 19863
