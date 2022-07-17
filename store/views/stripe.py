from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from store.models.product import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
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

        print(name)
        print(total)

        stripe_total = int(total * 100)
        stripe_name = ', '.join(str(s) for s in name)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': stripe_total,
                        'product_data': {
                            'name': stripe_name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/save/',
            cancel_url=YOUR_DOMAIN + '/cart/',

        )
        return JsonResponse({
            'id': checkout_session.id
        })


