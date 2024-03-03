class Product:
    def __init__(
        self,
        product_name: str,
        product_netto_price: float,
        product_percent_vat_rate: int,
    ):
        self.__product_name = product_name
        self.__product_netto_price = product_netto_price
        self.__product_percent_vat_rate = product_percent_vat_rate / 100

    def get_product_name(self):
        return self.__product_name

    def get_netto_price(self):
        return self.__product_netto_price

    def get_vat_rate(self):
        return self.__product_percent_vat_rate

    def calculate_vat_price(self):
        self.__product_vat_price = (
            self.__product_netto_price * self.__product_percent_vat_rate
        )

        return self.__product_vat_price
