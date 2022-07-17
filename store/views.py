from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json


def paymentComplete(request):
    body = json.loads(request)
    print('BODY', body)
    return JsonResponse('test')
