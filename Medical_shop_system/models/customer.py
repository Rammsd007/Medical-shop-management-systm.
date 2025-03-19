import sqlite3

class Customer:
    def __init__(self, customer_id=None, name="", email=""):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    @staticmethod
    def create_table():
        """Create the customers table in the database if it doesn't exist."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT UNIQUE
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        """Save the customer to the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        
        if self.customer_id is None:  # New customer
            c.execute('''
                INSERT INTO customers (name, email)
                VALUES (?, ?)
            ''', (self.name, self.email))
            self.customer_id = c.lastrowid  # Get the id of the newly inserted customer
        else:  # Existing customer
            c.execute('''
                UPDATE customers
                SET name = ?, email = ?
                WHERE id = ?
            ''', (self.name, self.email, self.customer_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_customer_by_id(customer_id):
        """Retrieve a customer from the database by their ID."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('''
            SELECT * FROM customers WHERE id = ?
        ''', (customer_id,))
        customer_data = c.fetchone()
        conn.close()

        if customer_data:
            return Customer(
                customer_id=customer_data[0],
                name=customer_data[1],
                email=customer_data[2]
            )
        return None

    @staticmethod
    def get_all_customers():
        """Retrieve all customers from the database."""
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()
        c.execute('SELECT * FROM customers')
        customers_data = c.fetchall()
        conn.close()

        customers = []
        for customer in customers_data:
            customers.append(Customer(
                customer_id=customer[0],
                name=customer[1],
                email=customer[2]
            ))
        return customers

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name={self.name}, email={self.email})"
