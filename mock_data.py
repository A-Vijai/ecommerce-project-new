import csv
import random
import string
from random import randint, choice


customer_ids = ["CUST00001", "CUST00002", "CUST00003", "CUST00004", "CUST00005"]
product_ids = ["PROD00001", "PROD00002", "PROD00003", "PROD00004", "PROD00005"]

payment_types = ["Credit Card", "Debit Card", "Cash on Delivery"]

transactions_per_day = 10

product_prices = {
    "PROD00001": 799.99,
    "PROD00002": 499.99,
    "PROD00003": 79.99,
    "PROD00004": 19.99,
    "PROD00005": 49.99,
    "PROD00006": 99.99,
    "PROD00007": 149.99,
    "PROD00008": 199.99,
    "PROD00009": 14.99,
    "PROD00010": 19.99,
}


def get_product_price(product_id):

    if product_id in product_prices:
        return product_prices[product_id]
    else:
        return 0.00


def generate_transaction(current_date, transaction_id_prefix='TXN'):
      transaction_id = f"{transaction_id_prefix}{''.join(random.choices(string.digits, k=8))}"
      customer_id = choice(customer_ids)
      product_id = choice(product_ids)
      quantity = randint(1, 5)  # Adjust quantity range as needed
      product_price = get_product_price(product_id)
      price = round(product_price * quantity, 2)  # Calculate total price
      transaction_date = str(current_date)
      payment_type = choice(payment_types)
      status = "Completed"
      return {
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "price": price,
            "transaction_date": transaction_date,
            "payment_type": payment_type,
            "status": status
        }


def generate_transactions(num_transactions, currrent_date):
    transactions=[]
    for _ in range(num_transactions):
        transactions.append(generate_transaction(currrent_date))
    return transactions


def write_to_csv(data,filename):

    with open(filename, 'w',newline="") as f:
        csv_writer=csv.DictWriter(f,fieldnames=["transaction_id", "customer_id", "product_id", "quantity",
                                                      "price", "transaction_date", "payment_type", "status"])
        csv_writer.writeheader()
        csv_writer.writerows(data)

    return



def generate_data(currrent_date,date_str):
    transactions=generate_transactions(transactions_per_day,currrent_date)
    write_to_csv(transactions,f"/tmp/transactions_{date_str}.csv")
    print(f"Generated mock transaction data transactions_{date_str}.csv and saved in csv files")
    return

