from django.views import View
from django.shortcuts import render
from store.models.category import Category
from store.models.product import Product


class Index(View):
    return_url = None

    def get(self, request):
        request.session['currency'] = {}
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
        Index.return_url = request.GET.get('return_url')
        return render(request, 'index.html', data)
