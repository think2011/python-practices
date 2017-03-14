from django.shortcuts import render, HttpResponse


def first_page(request):
    return HttpResponse('<p>西餐</p>')
