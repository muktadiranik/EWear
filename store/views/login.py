from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                request.session['first_name'] = customer.first_name
                request.session['last_name'] = customer.last_name
                request.session['phone'] = customer.phone

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('index')
            else:
                error_message = 'Invalid Email or Password'
        else:
            error_message = 'Invalid Email or Password'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def Logout(request):
    request.session.clear()
    return redirect('login')
