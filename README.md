# Trading Bot 🚀

**Author:** Harsh Verma  
**GitHub:** [https://github.com/harsh-12-dev/trading_bot](https://github.com/harsh-12-dev/trading_bot)  

---

## 1️⃣ Project Overview

Ye project ek **Python-based Binance trading bot** hai jo:

- Market orders place kar sakta hai (BUY/SELL)  
- Open positions fetch kar sakta hai  
- CLI (Command Line Interface) ke through control hota hai  
- Logs me sab activity save karta hai  
- Future me AI integration ke liye ready hai (market summary / trade suggestions)

---

## 2️⃣ Features

- ✅ Place MARKET orders  
- ✅ Fetch open positions  
- ✅ CLI-based commands  
- ✅ Logs folder me trading activity track  
- ✅ AI integration placeholder ready (for assessment demo)  

---

## 3️⃣ Tech Stack

| Layer        | Technology / Library                  |
|-------------|--------------------------------------|
| Backend      | Python + Binance API                  |
| CLI          | argparse (Python)                     |
| Logging      | Python logging module                  |
| Virtual Env  | venv                                   |
| AI Tools     | OpenAI API (optional, placeholder)   |

---

## 4️⃣ Folder Structure

```text
trading_bot/
 ├── bot/
 │    ├── __init__.py
 │    ├── client.py
 │    ├── orders.py
 │    └── logging_config.py
 ├── logs/                     # Trading logs
 ├── cli.py                     # CLI commands
 ├── requirements.txt
 └── test_connection.py         # Test Binance API connection
