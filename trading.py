
# import alpaca-py as alpaca  # Assuming you have the Alpaca API library installed
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

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
    api_key = "PKQVJGAODJ10MIPBG6AD"
    api_secret = "HfreSfxHl7hUL5Juga1b2pPSzjmfqQEMemT9Tgjl"
    return TradingClient(api_key, api_secret)


def get_market_data():
# Simulate retrieving market data (replace with actual API calls)
    api_key = "PKQVJGAODJ10MIPBG6AD"
    api_secret = "HfreSfxHl7hUL5Juga1b2pPSzjmfqQEMemT9Tgjl"
    trading_client = TradingClient(api_key, api_secret)
# search for US equities
    search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
    assets = trading_client.get_all_assets(search_params)
# data = {"open": 100, "high": 110, "low": 90, "close": 105}
    print(assets)
    return assets


get_market_data()

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




