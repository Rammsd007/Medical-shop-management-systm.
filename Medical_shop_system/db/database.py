import sqlite3

def create_db():
    try:
        # Connect to the database (it will create the file if it doesn't exist)
        conn = sqlite3.connect('medical_shop.db')
        c = conn.cursor()

        # Create the 'products' table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                price REAL,
                quantity INTEGER
            )
        ''')

        # Create the 'customers' table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                address TEXT
            )
        ''')

        # Create the 'sales' table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                customer_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                sale_date TEXT,
                FOREIGN KEY(product_id) REFERENCES products(id),
                FOREIGN KEY(customer_id) REFERENCES customers(id)
            )
        ''')

        # Commit the changes to the database
        conn.commit()

    except sqlite3.Error as e:
        # Catch any errors related to SQLite and print a message
        print(f"SQLite error: {e}")
    
    finally:
        # Ensure the connection is closed, whether an error occurred or not
        conn.close()

# Call the function to create the database and tables
create_db()
