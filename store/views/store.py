from django.shortcuts import render, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Store(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
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
        print('cart', request.session['cart'])

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()

        data = {'products': products, 'categories': categories}
        print('email', request.session.get('email'))
        print('first_name', request.session.get('first_name'))
        return render(request, 'store.html', data)
