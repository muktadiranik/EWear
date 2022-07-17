from django.shortcuts import redirect
from django.views import View


class Check(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        request.session['address'] = address
        request.session['phone'] = phone

        return redirect('payment')
