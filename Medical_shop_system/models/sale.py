import sqlite3
from datetime import datetime

class Sale:
    def __init__(self, sale_id=None, customer_id=None, product_id=None, quantity=0, total_price=0.0, sale_date=None):
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.sale_date = sale_date if sale_date else datetime.now()

    @staticmethod
    def create_table():
        """Create the sales table in the database if it does not exist."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                sale_date TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        """Save the sale to the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        
        # Insert sale details into the sales table
        c.execute('''
            INSERT INTO sales (customer_id, product_id, quantity, total_price, sale_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.customer_id, self.product_id, self.quantity, self.total_price, self.sale_date))

        conn.commit()
        conn.close()

    @staticmethod
    def get_sale_by_id(sale_id):
        """Retrieve a sale from the database by its ID."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            SELECT * FROM sales WHERE id = ?
        ''', (sale_id,))
        sale_data = c.fetchone()
        conn.close()

        if sale_data:
            return Sale(
                sale_id=sale_data[0],
                customer_id=sale_data[1],
                product_id=sale_data[2],
                quantity=sale_data[3],
                total_price=sale_data[4],
                sale_date=sale_data[5]
            )
        return None

    @staticmethod
    def get_all_sales():
        """Retrieve all sales from the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('SELECT * FROM sales')
        sales_data = c.fetchall()
        conn.close()

        sales = []
        for sale in sales_data:
            sales.append(Sale(
                sale_id=sale[0],
                customer_id=sale[1],
                product_id=sale[2],
                quantity=sale[3],
                total_price=sale[4],
                sale_date=sale[5]
            ))
        return sales

    @staticmethod
    def update_sale(sale_id, quantity, total_price):
        """Update an existing sale in the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            UPDATE sales
            SET quantity = ?, total_price = ?
            WHERE id = ?
        ''', (quantity, total_price, sale_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_sale(sale_id):
        """Delete a sale from the database by its ID."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            DELETE FROM sales WHERE id = ?
        ''', (sale_id,))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"Sale(id={self.sale_id}, customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity}, total_price={self.total_price}, sale_date={self.sale_date})"
