import re
from datetime import datetime

def is_valid_email(email):
    """
    Validate if the provided email address is in a correct format.
    Returns True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def format_date(date_obj):
    """
    Format a datetime object to a string in the format: YYYY-MM-DD HH:MM:SS
    """
    if isinstance(date_obj, datetime):
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')
    return None

def calculate_total_price(price_per_unit, quantity):
    """
    Calculate the total price for a given quantity of a product.
    """
    try:
        total_price = price_per_unit * quantity
        return round(total_price, 2)  # rounding to 2 decimal places
    except Exception as e:
        print(f"Error calculating total price: {e}")
        return 0.0

def get_current_datetime():
    """
    Return the current date and time as a string.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def is_positive_integer(value):
    """
    Check if the provided value is a positive integer.
    """
    try:
        return isinstance(int(value), int) and int(value) > 0
    except ValueError:
        return False

def sanitize_input(user_input):
    """
    Sanitize user input to prevent SQL injection and malicious characters.
    """
    # A simple example to remove unwanted characters (you can extend this based on your needs).
    sanitized_input = re.sub(r'[^\w\s]', '', user_input)
    return sanitized_input

def print_invoice(invoice_data):
    """
    Print a formatted invoice from the given data (like a sale or purchase).
    """
    print("\n--- Invoice ---")
    print(f"Sale Date: {invoice_data['sale_date']}")
    print(f"Customer: {invoice_data['customer_name']}")
    print(f"Product: {invoice_data['product_name']}")
    print(f"Quantity: {invoice_data['quantity']}")
    print(f"Total Price: ${invoice_data['total_price']}")
    print(f"Thank you for shopping with us!\n")
