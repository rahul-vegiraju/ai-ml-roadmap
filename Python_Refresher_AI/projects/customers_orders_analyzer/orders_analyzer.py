import csv


def read_orders(filename):
    orders = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            order = {
                "customer": row["customer"],
                "product": row["product"],
                "category": row["category"],
                "quantity": int(row["quantity"]),
                "price": float(row["price"])
            }
            orders.append(order)

    return orders


def total_revenue(orders):
    total = 0

    for order in orders:
        total += order["quantity"] * order["price"]

    return total


def product_revenue(orders):
    totals = {}

    for order in orders:
        product = order["product"]
        revenue = order["quantity"] * order["price"]

        if product not in totals:
            totals[product] = 0

        totals[product] += revenue

    return totals


def customer_totals(orders):
    totals = {}

    for order in orders:
        customer = order["customer"]
        revenue = order["quantity"] * order["price"]

        if customer not in totals:
            totals[customer] = 0

        totals[customer] += revenue

    return totals


def category_totals(orders):
    totals = {}

    for order in orders:
        category = order["category"]
        revenue = order["quantity"] * order["price"]

        if category not in totals:
            totals[category] = 0

        totals[category] += revenue

    return totals


def sort_totals(totals):
    return sorted(totals.items(), key=lambda item: item[1], reverse=True)


def write_report(orders, filename):
    revenue = total_revenue(orders)
    products = sort_totals(product_revenue(orders))
    customers = sort_totals(customer_totals(orders))
    categories = sort_totals(category_totals(orders))

    with open(filename, "w") as report:
        report.write("Customer Orders Report\n")
        report.write("----------------------\n")
        report.write(f"Total Revenue: ${revenue:.2f}\n")
        report.write(f"Total Orders: {len(orders)}\n\n")

        report.write("Top Products by Revenue:\n")
        for product, amount in products:
            report.write(f"- {product}: ${amount:.2f}\n")

        report.write("\nTop Customers by Spending:\n")
        for customer, amount in customers:
            report.write(f"- {customer}: ${amount:.2f}\n")

        report.write("\nCategory Totals:\n")
        for category, amount in categories:
            report.write(f"- {category}: ${amount:.2f}\n")


orders = read_orders("Python_Refresher_AI/projects/customers_orders_analyzer/sample.csv")
write_report(orders, "Python_Refresher_AI/projects/customers_orders_analyzer/orders_report.txt")

print("Report created successfully.")