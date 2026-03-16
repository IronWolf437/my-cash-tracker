# MyCashTracker

A simple Python CLI tool to track physical pocket cash. Designed to work on Linux and Android (Termux).

## Why this exists?

When you're out and spending cash, it's hard to keep track of exactly how much is left in your pocket without counting it every time. This tool acts as a digital mirror for your physical pocket, allowing you to log expenses and additions on the fly.

## Features

* Track spending and additions in real-time.
* Manual balance correction to sync with actual cash.
* Logs all transactions to a `data.csv` file with timestamps.
* Simple terminal interface with color-coded warnings.

## Usage

1. Run the script:
```bash
python3 money.py

```


2. Enter your initial budget for the current session.
3. Use the following keys:
* `a`: Add money.
* `s`: Spend money.
* `c`: Check current balance.
* `k`: Correct account balance.
* `d`: Display transaction history.
* `q`: Save and quit.



## Requirements

* Python 3.x
* Standard libraries: `time`, `csv`
