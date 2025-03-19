from models.product import Product

def add_product(name, price, quantity):
    product = Product(name=name, price=price, quantity=quantity)
    product.save()

def get_all_products():
    return Product.get_all_products()

def get_product_by_id(product_id):
    return Product.get_product_by_id(product_id)

def update_product(product_id, price=None, quantity=None):
    product = Product.get_product_by_id(product_id)
    if price:
        product.price = price
    if quantity:
        product.quantity = quantity
    product.save()
