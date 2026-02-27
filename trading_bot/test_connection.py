from binance.client import Client
from binance.exceptions import BinanceAPIException

api_key = "OVZ4VPJZ5hvswOZpuf3RoMU1F4TGThHuaSv88W9zixkw4VVSNbQQ7BgPZPfm9ZaS"
api_secret = "nmQTWhd0pXb70KkvdseOZ6IIw4B9XIBwjNeTHKNHebRV4wUKxeW1tMR3gmeNipCe"

client = Client(api_key, api_secret, testnet=True)

try:
    print("Placing MARKET order...")

    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.003
    )

    print("✅ Order placed successfully!")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
    print("Executed Qty:", order["executedQty"])

except BinanceAPIException as e:
    print("❌ Binance API Error:", e.message)

except Exception as e:
    print("❌ Error:", str(e))