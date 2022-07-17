from django.views import View
from django.shortcuts import render


class Profile(View):
    def get(self, request):
        customer = request.session.get('customer')
        first_name = request.session.get('first_name')
        last_name = request.session.get('last_name')
        email = request.session.get('email')
        phone = request.session.get('phone')
        return render(request, 'profile.html')
