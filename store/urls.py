from django.urls import path
from .views.index import Index
from .views.store import Store
from .views.signup import Signup
from .views.login import Login, Logout
from .views.cart import Cart
from .views.save import save
from .views.orders import OrderView
from .views.checkout import Checkout
from .views.profile import Profile
from .middlewares.auth import auth_middleware
from .views.stripe import CreateCheckoutSessionView
from .views.webhook import stripe_webhook

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('store/', Store.as_view(), name='store'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    path('cart/', auth_middleware(Cart.as_view()), name='cart'),
    path('save/', save, name='save'),
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook')
]
