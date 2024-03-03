from product import Product


class Receipt:
    def __init__(self, product_list: list):
        self.__product_list = product_list

    def get_product_list(self):
        return self.__product_list

    def add_receipt_position(self, product: Product):
        self.__product_list.append(product)

    def calculate_total_netto_sum(self):
        return sum([product.get_netto_price() for product in self.__product_list])

    def calculate_total_vat_sum(self, vat_rate):
        return sum(
            [
                product.calculate_vat_price()
                for product in self.__product_list
                if product.get_vat_rate() == vat_rate
            ]
        )
