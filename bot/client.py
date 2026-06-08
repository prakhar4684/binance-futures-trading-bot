import os
from dotenv import load_dotenv
from binance.client import Client


load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
secret = os.getenv("BINANCE_SECRET_KEY")
print("KEY:", api_key)
print("SECRET:", secret)
class BinanceClient:


    def __init__(self):

        api_key = os.getenv(
            "BINANCE_API_KEY"
        )

        secret = os.getenv(
            "BINANCE_SECRET_KEY"
        )


        self.client = Client(
            api_key,
            secret,
            testnet=True
        )


        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com"
        )


    def get_client(self):

        return self.client