from models.sale import Sale
from models.product import Product
from models.customer import Customer
from utils.helpers import calculate_total_price
from datetime import datetime

def record_sale(customer_id, product_id, quantity):
    customer = Customer.get_customer_by_id(customer_id)
    product = Product.get_product_by_id(product_id)

    if customer and product and product.quantity >= quantity:
        total_price = calculate_total_price(product.price, quantity)
        sale = Sale(customer_id=customer.customer_id, product_id=product.product_id, quantity=quantity, total_price=total_price, sale_date=datetime.now())
        sale.save()
        
        # Update product quantity
        product.quantity -= quantity
        product.save()

        return sale
    return None

def get_all_sales():
    return Sale.get_all_sales()
