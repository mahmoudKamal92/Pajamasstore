from django.shortcuts import render
from .models import *

# Create your views here.
def product_list (request):
    context = ()
    return render(request, 'index.html' )




def product_details (requst):
    pass