import sqlite3

class Product:
    def __init__(self, product_id=None, name="", price=0.0, quantity=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def create_table():
        """Create the products table in the database if it doesn't exist."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                quantity INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        """Save the product to the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        
        if self.product_id is None:  # New product
            c.execute('''
                INSERT INTO products (name, price, quantity)
                VALUES (?, ?, ?)
            ''', (self.name, self.price, self.quantity))
            self.product_id = c.lastrowid  # Get the id of the newly inserted product
        else:  # Existing product
            c.execute('''
                UPDATE products
                SET name = ?, price = ?, quantity = ?
                WHERE id = ?
            ''', (self.name, self.price, self.quantity, self.product_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_product_by_id(product_id):
        """Retrieve a product from the database by its ID."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            SELECT * FROM products WHERE id = ?
        ''', (product_id,))
        product_data = c.fetchone()
        conn.close()

        if product_data:
            return Product(
                product_id=product_data[0],
                name=product_data[1],
                price=product_data[2],
                quantity=product_data[3]
            )
        return None

    @staticmethod
    def get_all_products():
        """Retrieve all products from the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('SELECT * FROM products')
        products_data = c.fetchall()
        conn.close()

        products = []
        for product in products_data:
            products.append(Product(
                product_id=product[0],
                name=product[1],
                price=product[2],
                quantity=product[3]
            ))
        return products

    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, quantity={self.quantity})"
