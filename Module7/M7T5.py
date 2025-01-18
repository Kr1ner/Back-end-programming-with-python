import csv
import json
import pickle
from typing import List, Optional

class BaseEntity:
    @classmethod
    def save_csv(cls, filename: str, items: List[dict]):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)

    @classmethod
    def load_csv(cls, filename: str) -> List[dict]:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @classmethod
    def save_json(cls, filename: str, items: List[dict]):
        with open(filename, mode='w') as file:
            json.dump(items, file, indent=4)

    @classmethod
    def load_json(cls, filename: str) -> List[dict]:
        with open(filename, mode='r') as file:
            return json.load(file)

    @classmethod
    def save_pickle(cls, filename: str, items: List[dict]):
        with open(filename, mode='wb') as file:
            pickle.dump(items, file)

    @classmethod
    def load_pickle(cls, filename: str) -> List[dict]:
        with open(filename, mode='rb') as file:
            return pickle.load(file)

class Product(BaseEntity):
    def __init__(self, product_id: int, name: str, category: 'Category', product_model: Optional['ProductModel'] = None):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.product_model = product_model

class Category(BaseEntity):
    def __init__(self, category_id: int, name: str, parent_category: Optional['Category'] = None):
        self.category_id = category_id
        self.name = name
        self.parent_category = parent_category
        self.sub_categories: List['Category'] = []

    def add_sub_category(self, sub_category: 'Category'):
        self.sub_categories.append(sub_category)

class Customer(BaseEntity):
    def __init__(self, customer_id: int, first_name: str, last_name: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.addresses: List['Address'] = []
        self.orders: List['Order'] = []

    def add_address(self, address: 'Address'):
        self.addresses.append(address)

    def add_order(self, order: 'Order'):
        self.orders.append(order)

class Address(BaseEntity):
    def __init__(self, address_id: int, address_line1: str, city: str, state_province: str, postal_code: str):
        self.address_id = address_id
        self.address_line1 = address_line1
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code

class CustomerAddress(BaseEntity):
    def __init__(self, customer: Customer, address: Address, address_type: str):
        self.customer = customer
        self.address = address
        self.address_type = address_type

class Order(BaseEntity):
    def __init__(self, order_id: int, order_date: str, customer: Customer, ship_to: Address, bill_to: Address):
        self.order_id = order_id
        self.order_date = order_date
        self.customer = customer
        self.ship_to = ship_to
        self.bill_to = bill_to
        self.order_details: List['OrderDetail'] = []

    def add_order_detail(self, order_detail: 'OrderDetail'):
        self.order_details.append(order_detail)

class OrderDetail(BaseEntity):
    def __init__(self, order: Order, product: Product, quantity: int, unit_price: float):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.line_total = self.quantity * self.unit_price

class ProductModel(BaseEntity):
    def __init__(self, product_model_id: int, name: str, catalog_description: Optional[str] = None):
        self.product_model_id = product_model_id
        self.name = name
        self.catalog_description = catalog_description

if __name__ == "__main__":
    category = Category(1, "Electronics")
    product_model = ProductModel(1, "Smartphone Model X")
    product = Product(1, "Smartphone", category, product_model)

    customer = Customer(1, "John", "Doe")
    address = Address(1, "123 Main St", "Springfield", "IL", "62701")
    customer.add_address(address)

    order = Order(1, "2025-01-01", customer, address, address)
    order_detail = OrderDetail(order, product, 2, 599.99)
    order.add_order_detail(order_detail)

    customers = [vars(customer)]
    Customer.save_json("customers.json", customers)
    loaded_customers = Customer.load_json("customers.json")
    print(loaded_customers)
