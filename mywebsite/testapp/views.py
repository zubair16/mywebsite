from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    # template = loader.get_template('testapp/index.html')
    return render(request, 'testapp/index.html')
