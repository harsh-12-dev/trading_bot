from binance.client import Client
import os

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_SECRET_KEY")

        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found in environment variables")

        self.client = Client(self.api_key, self.api_secret, testnet=True)

    def get_account_info(self):
        return self.client.futures_account()

    def create_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)

    # ✅ ADD THIS
    def get_positions(self):
        return self.client.futures_position_information()