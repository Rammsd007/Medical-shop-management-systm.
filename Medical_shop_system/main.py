import os
import re
from models.product import Product
from models.customer import Customer
from models.sale import Sale
from utils.helpers import calculate_total_price, print_invoice, is_positive_integer, get_current_datetime


def display_menu():
    Product.create_table()
    Customer.create_table()
    Sale.create_table()
    """
    Displays the main menu of the Medical Shop Management System.
    """
    print("\n--- Medical Shop Management System ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Add Customer")
    print("5. View Customers")
    print("6. Record Sale")
    print("7. View Sales")
    print("8. Generate Invoice")
    print("9. Exit")
    print("----------------------------------------")


def add_product():
    """
    Add a new product to the inventory.
    """
    print("\n--- Add Product ---")
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")

    if not is_positive_integer(price) or not is_positive_integer(quantity):
        print("Invalid input. Price and quantity must be positive integers.")
        return

    product = Product(name=name, price=float(price), quantity=int(quantity))
    # product.create_table()
    product.save()
    print(f"Product '{name}' added successfully.")


def view_products():
    """
    View all products in the inventory.
    """
    print("\n--- View Products ---")
    products = Product.get_all_products()

    if not products:
        print("No products available in the inventory.")
    else:
        for product in products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")


def update_product():
    """
    Update the details of an existing product.
    """
    print("\n--- Update Product ---")
    product_id = input("Enter product ID to update: ")

    if not is_positive_integer(product_id):
        print("Invalid input. Product ID must be a positive integer.")
        return

    product = Product.get_product_by_id(int(product_id))
    if not product:
        print(f"Product with ID {product_id} not found.")
        return

    print(f"Current details of product '{product.name}': Price: ${product.price}, Quantity: {product.quantity}")
    new_price = input("Enter new price (or leave blank to keep current): ")
    new_quantity = input("Enter new quantity (or leave blank to keep current): ")

    if new_price:
        product.price = float(new_price)
    if new_quantity:
        product.quantity = int(new_quantity)

    product.save()
    print(f"Product '{product.name}' updated successfully.")


def add_customer():
    """
    Add a new customer to the system.
    """
    print("\n--- Add Customer ---")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")

    if not is_valid_email(email):
        print("Invalid email address. Please provide a valid email.")
        return

    customer = Customer(name=name, email=email)
    customer.save()
    print(f"Customer '{name}' added successfully.")


def view_customers():
    """
    View all customers in the system.
    """
    print("\n--- View Customers ---")
    customers = Customer.get_all_customers()

    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}")


def record_sale():
    """
    Record a new sale transaction.
    """
    print("\n--- Record Sale ---")
    customer_id = input("Enter customer ID: ")
    product_id = input("Enter product ID: ")
    quantity = input("Enter quantity: ")

    if not is_positive_integer(customer_id) or not is_positive_integer(product_id) or not is_positive_integer(quantity):
        print("Invalid input. IDs and quantity must be positive integers.")
        return

    customer = Customer.get_customer_by_id(int(customer_id))
    product = Product.get_product_by_id(int(product_id))

    if not customer:
        print(f"Customer with ID {customer_id} not found.")
        return

    if not product:
        print(f"Product with ID {product_id} not found.")
        return

    if int( quantity) > product.quantity:
        print(f"Insufficient quantity for product '{product.name}'.")
        return

    total_price = calculate_total_price(product.price, int(quantity))
     # Create the sale record
    sale = Sale(customer_id=customer.customer_id, product_id=product.product_id, quantity=int(quantity),
                total_price=total_price, sale_date=get_current_datetime())
    sale.save()


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


 
 # Create the sale record
    sale = Sale(customer_id=customer.customer_id, product_id=product.product_id, quantity=int(quantity),
                total_price=total_price, sale_date=get_current_datetime())
    sale.save()

    # Update product quantity
    product.quantity -= int(quantity)
    product.save()

    print(f"Sale recorded successfully! Total Price: ${total_price}")


def view_sales():
    """
    View all sales transactions.
    """
    print("\n--- View Sales ---")
    sales = Sale.get_all_sales()

    if not sales:
        print("No sales recorded.")
    else:
        for sale in sales:
            print(f"Sale ID: {sale.sale_id}, Customer ID: {sale.customer_id}, Product ID: {sale.product_id}, "
                  f"Quantity: {sale.quantity}, Total Price: ${sale.total_price}, Date: {sale.sale_date}")

def generate_invoice():
    """
    Generate and print an invoice for a sale.
    """
    print("\n--- Generate Invoice ---")
    sale_id = input("Enter sale ID to generate invoice: ")

    if not is_positive_integer(sale_id):
        print("Invalid input. Sale ID must be a positive integer.")
        return

    sale = Sale.get_sale_by_id(int(sale_id))

    if not sale:
        print(f"Sale with ID {sale_id} not found.")
        return

    # Prepare invoice data
    customer = Customer.get_customer_by_id(sale.customer_id)
    product = Product.get_product_by_id(sale.product_id)

    invoice_data = {
        "sale_date": sale.sale_date,
        "customer_name": customer.name,
        "product_name": product.name,
        "quantity": sale.quantity,
        "total_price": sale.total_price
    }

    print_invoice(invoice_data)


def main():
    """
    Main function to start the Medical Shop Management System.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            add_customer()
        elif choice == '5':
            view_customers()
        elif choice == '6':
            record_sale()
        elif choice == '7':
            view_sales()
        elif choice == '8':
            generate_invoice()
        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()