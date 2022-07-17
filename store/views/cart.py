from django.views import View
from django.shortcuts import render, HttpResponseRedirect
from store.models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        cart = request.session.get('cart')
        total = 0
        name = []
        for product in products:
            quantity = cart.get(str(product.id))
            price = product.price * quantity
            total = total + price
            name.append(product.name)

        string_name = ', '.join(str(s) for s in name)
        print(total)
        print(string_name)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        customer = request.session.get('customer')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        request.session['address'] = address
        request.session['phone'] = phone
        print('cart', request.session['cart'])

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
