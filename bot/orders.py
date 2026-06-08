class OrderManager:


    def __init__(
        self,
        client,
        logger
    ):

        self.client = client
        self.logger = logger



    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            data = {

                "symbol":symbol,
                "side":side,
                "type":order_type,
                "quantity":quantity
            }


            if order_type=="LIMIT":

                data["price"]=price
                data["timeInForce"]="GTC"



            self.logger.info(
                f"REQUEST {data}"
            )



            response = (
                self.client
                .futures_create_order(
                    **data
                )
            )


            self.logger.info(
                f"RESPONSE {response}"
            )


            return response


        except Exception as e:


            self.logger.error(
                str(e)
            )


            raise e