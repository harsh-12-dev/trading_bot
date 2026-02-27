from binance.exceptions import BinanceAPIException
from bot.logging_config import logger

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Market Order placed: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Market Order): {e.message}")
            raise Exception(f"Binance API Error: {e.message}")

        except Exception as e:
            logger.error(f"Unexpected Error (Market Order): {str(e)}")
            raise Exception(f"Unexpected Error: {str(e)}")


    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Limit Order placed: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Limit Order): {e.message}")
            raise Exception(f"Binance API Error: {e.message}")

        except Exception as e:
            logger.error(f"Unexpected Error (Limit Order): {str(e)}")
            raise Exception(f"Unexpected Error: {str(e)}")


    # ✅ NEW FUNCTION: Get Open Positions
    def get_open_positions(self):
        try:
            positions = self.client.get_positions()

            # Sirf active positions filter karenge
            active_positions = [
                p for p in positions if float(p["positionAmt"]) != 0
            ]

            logger.info("Fetched open positions")

            return active_positions

        except Exception as e:
            logger.error(f"Error fetching positions: {str(e)}")
            raise Exception(f"Error fetching positions: {str(e)}")