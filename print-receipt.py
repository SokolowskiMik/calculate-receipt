from product import Product
from receipt import Receipt


def generate_summary(receipt):
    markdown_table = "|               | Total netto |     X     |\n|---------------|-------------|-----------|\n"

    unique_vat_rates = set(
        product.get_vat_rate() for product in receipt.get_product_list()
    )

    for vat_rate in sorted(unique_vat_rates):
        netto = receipt.calculate_total_netto_sum()
        vat_sum = receipt.calculate_total_vat_sum(vat_rate)

        markdown_table += f"| VAT {vat_rate*100}%        | {netto:10.2f} zl   | {vat_sum:9.2f} zl  |\n"

    return markdown_table


def save_receipt_to_file(markdown_content, file_name="summary.md"):
    with open(file_name, "w") as file:
        file.write(markdown_content)


# Dane wejściowe
product_list = [
    Product("Clean Code, Robert C. Martin", 100.00, 8),
    Product("Applying UML and Patterns, C. Larman", 300.00, 8),
    Product("Shipping", 50.00, 23),
]

receipt = Receipt(product_list)

markdown_content = generate_summary(receipt)

save_receipt_to_file(markdown_content)
