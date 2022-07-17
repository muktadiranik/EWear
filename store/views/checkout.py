from django.shortcuts import redirect
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product
from django.shortcuts import render
from django.views import View


class Checkout(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'checkout.html', {'products': products})

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        request.session['address'] = address
        request.session['phone'] = phone

        return redirect('checkout')


class SaveOrder(View):
    def post(self, request):
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
