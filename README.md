# Weirwood PyFinance

[![Build Status](https://github.com/weirwoodai/weirwood_pyfinance/workflows/Build%20Main/badge.svg)](https://github.com/weirwoodai/weirwood_pyfinance/actions)

Python API for downloading stock prices and fundamental accounting concepts

---

## Installation

**Stable Release:** `weirwood-pyfinance`<br>

```console
> pip install weirwood-pyfinance
```

**Development Head:** `git+https://github.com/weirwoodai/weirwood_pyfinance.git`

```console
> pip install git+https://github.com/weirwoodai/weirwood_pyfinance.git
```

## Quick Start

Register your account at https://weirwood.ai for free

```python
from weirwood_pyfinance import FinTen

finten = FinTen()
finten.set_login(username="<YOUR USERNAME>",password="<YOUR PASSWORD>")
filings = finten.get_filings(ticker="AAPL")
prices = finten.get_prices(ticker="AAPL")
```

If you don't have an account you can still access using the free tier

```python
from weirwood_pyfinance import FinTen

finten = FinTen()
filings = finten.get_filings(ticker="AAPL")
prices = finten.get_prices(ticker="AAPL")
```

**MIT license**
