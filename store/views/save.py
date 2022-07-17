from django.shortcuts import redirect
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product


def save(request):
    address = request.session.get('address')
    phone = request.session.get('phone')
    customer = request.session.get('customer')
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    print(address, phone, customer, cart, products)

    for product in products:
        print(cart.get(str(product.id)))
        order = Order(customer=Customer(id=customer),
                      product=product,
                      price=product.price,
                      address=address,
                      phone=phone,
                      quantity=cart.get(str(product.id)))
        order.save()
    request.session['cart'] = {}
    request.session['address'] = {}
    request.session['phone'] = {}

    return redirect('orders')
