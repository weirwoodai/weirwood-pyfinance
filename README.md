# Weirwood PyFinance

[![Build Status](https://github.com/weirwoodai/weirwood_pyfinance/workflows/Build%20Main/badge.svg)](https://github.com/weirwoodai/weirwood_pyfinance/actions)
[![Documentation](https://github.com/weirwoodai/weirwood_pyfinance/workflows/Documentation/badge.svg)](https://weirwoodai.github.io/weirwood_pyfinance/)
[![Code Coverage](https://codecov.io/gh/weirwoodai/weirwood_pyfinance/branch/main/graph/badge.svg)](https://codecov.io/gh/weirwoodai/weirwood_pyfinance)

Python API for downloading stock prices and fundamental accounting concepts

---

## Quick Start

```python
from weirwood_pyfinance import Finten

finten = FinTen()
finten.set_login(username="<YOUR USERNAME>",password="<YOUR PASSWORD>")
filings = finten.get_filings(ticker="AAPL")
prices = FinTen().get_prices(ticker="AAPL")

```

## Installation

**Stable Release:** `pip install weirwood_pyfinance`<br>
**Development Head:** `pip install git+https://github.com/weirwoodai/weirwood_pyfinance.git`

**MIT license**
