
# import alpaca-py as alpaca  # Assuming you have the Alpaca API library installed
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient


# from .alpaca-trade-api import alpaca_trading

print("Hello")

# try:
#     import alpaca-py
# except Exception as e:
#     print(e)
def get_alpaca_api():
    # BASE_URL = "https://paper-api.alpaca.markets"
    # ALPACA_API_KEY = "<YOUR ALPACA API KEY>"
    # ALPACA_SECRET_KEY = "<YOUR ALPACA SECRET KEY>"
    # Replace with your actual Alpaca API key and secret (DO NOT SHARE THIS INFORMATION)
    api_key = "AKU1KJ87ZGWXEX727TEO"
    api_secret = "FvNdukxPK2hV6D2AdejUrYmPVkXa4QW56HUJVNLB"
    return TradingClient(api_key, api_secret)

print(get_alpaca_api())

# def get_market_data(client, symbol):
#     # Simulate retrieving market data (replace with actual API calls)
#     data = {"open": 100, "high": 110, "low": 90, "close": 105}
#     return data

# def make_trade_decision(data):
#     # Simulate a trading decision (replace with your trading strategy logic)
#     # **Important:** This is for educational purposes only and should not be used for actual trading
#     if data["close"] > data["open"]:
#         return "buy"
#     else:
#         return "sell"

# def simulate_trade(client, symbol, action):
#     # Simulate placing a trade (replace with actual order logic)
#     # **Important:** This does not involve actual trading and should not be used for real-world scenarios
#     print(f"Simulated {action} order for {symbol}")

# def main():
#     client = get_alpaca_api()
#     symbol = "AAPL"  # Example symbol

#     # Simulate getting market data
#     market_data = get_market_data(client, symbol)

#     # Simulate making a trade decision (replace with your trading strategy)
#     trade_decision = make_trade_decision(market_data)

#     # Simulate placing a trade (replace with actual order logic)
#     simulate_trade(client, symbol, trade_decision)

# if __name__ == "__main__":
#     main()
