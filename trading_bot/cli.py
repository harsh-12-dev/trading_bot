import argparse
from bot.client import BinanceFuturesClient
from bot.orders import OrderService

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")
    parser.add_argument("--positions", action="store_true", help="Check open positions")

    args = parser.parse_args()

    try:
        client = BinanceFuturesClient()
        order_service = OrderService(client)

        # ✅ POSITIONS FEATURE
        if args.positions:
            positions = order_service.get_open_positions()

            if not positions:
                print("\n📊 No open positions.")
            else:
                print("\n📊 Open Positions:")
                for p in positions:
                    print(f"""
Symbol: {p['symbol']}
Position Amt: {p['positionAmt']}
Entry Price: {p['entryPrice']}
Unrealized PnL: {p['unRealizedProfit']}
""")
            return  # Exit after showing positions

        # ✅ VALIDATION FOR ORDERS
        if not all([args.symbol, args.side, args.type, args.quantity]):
            raise ValueError("Symbol, side, type, and quantity are required for placing orders")

        print("\n📌 Order Request Summary")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)

        if args.type == "LIMIT":
            if not args.price:
                raise ValueError("Price is required for LIMIT orders")
            print("Price:", args.price)

        if args.type == "MARKET":
            order = order_service.place_market_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )
        else:
            order = order_service.place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        print("\n✅ Order Placed Successfully!")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))

    except Exception as e:
        print("\n❌ Error:", str(e))


if __name__ == "__main__":
    main()