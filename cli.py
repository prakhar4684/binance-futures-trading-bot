import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_order
from bot.logging_config import setup_logger



parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)


parser.add_argument("--symbol",
required=True)


parser.add_argument("--side",
required=True)


parser.add_argument("--type",
required=True)


parser.add_argument(
"--quantity",
type=float,
required=True
)


parser.add_argument(
"--price",
type=float
)



args = parser.parse_args()



try:


    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )



    logger = setup_logger()


    client = (
        BinanceClient()
        .get_client()
    )


    manager = OrderManager(
        client,
        logger
    )


    response = manager.place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )



    print("\nORDER SUCCESSFUL\n")


    print(
        "Order ID:",
        response.get("orderId")
    )


    print(
        "Status:",
        response.get("status")
    )


    print(
        "Executed Qty:",
        response.get("executedQty")
    )


    print(
        "Average Price:",
        response.get("avgPrice")
    )



except Exception as e:


    print(
        "ORDER FAILED:",
        e
    )