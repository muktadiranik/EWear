from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('login')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 characters long or more"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 characters long or more"
        elif not customer.phone:
            error_message = "Phone Number Required"
        elif len(customer.phone) < 11:
            error_message = "Phone Number must 11 digits long or more"
        elif not customer.email:
            error_message = "Email Required"
        elif len(customer.email) < 11:
            error_message = "Email must 11 characters long or more"
        elif not customer.password:
            error_message = "Password Required"
        elif len(customer.password) < 8:
            error_message = "Password must be 8 characters long or more"
        elif customer.isExists():
            error_message = "Email Already Exists"

        return error_message
