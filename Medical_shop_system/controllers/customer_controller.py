from models.customer import add_customer, view_customers

def add_new_customer(name, phone, address):
    """
    Add a new customer to the database.
    """
    add_customer(name, phone, address)

def display_all_customers():
    """
    Display all customers stored in the database.
    """
    customers = view_customers()
    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}, Address: {customer[3]}")
