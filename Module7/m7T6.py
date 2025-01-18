import sqlite3
from typing import List, Any, Dict, Optional

class BaseRepository:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create(self, **fields):
        columns = ', '.join(fields.keys())
        placeholders = ', '.join('?' for _ in fields)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, tuple(fields.values()))
            conn.commit()

    def get_all(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name}"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

    def get_by_id(self, record_id: int) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (record_id,))
            row = cursor.fetchone()
            if row:
                return dict(zip([column[0] for column in cursor.description], row))
            return None

    def update(self, record_id: int, **fields):
        updates = ', '.join(f"{key} = ?" for key in fields)
        query = f"UPDATE {self.table_name} SET {updates} WHERE id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, tuple(fields.values()) + (record_id,))
            conn.commit()

    def delete_by_id(self, record_id: int):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (record_id,))
            conn.commit()

class ProductRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Product")

class CategoryRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Category")

class CustomerRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Customer")

class AddressRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Address")

class CustomerAddressRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "CustomerAddress")

class OrderRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Order")

class OrderDetailRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "OrderDetail")

class ProductModelRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "ProductModel")

if __name__ == "__main__":
    db_name = "ecommerce.db"
    product_repo = ProductRepository(db_name)
    with product_repo.connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category_id INTEGER,
                product_model_id INTEGER
            )
        """)
    product_repo.create(name="Sample Product", category_id=1, product_model_id=1)
    products = product_repo.get_all()
    print(products)
    product = product_repo.get_by_id(1)
    print(product)
    product_repo.update(1, name="Updated Product")
    product_repo.delete_by_id(1)
