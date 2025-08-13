from django.shortcuts import render
from .models import Store, Item
# Create your views here.


def store_home(request, *args, **kwargs):

    context = {}

    return render (request, 'store/store_home.html', context)


def stores_view(request, *args, **kwargs):
    stores = Store.objects.all()

    context = {'stores':stores}

    return render (request, 'store/stores_view.html', context)


def items_view(request, *args, **kwargs):
    item = Item.objects.all()

    context = {'item':item}

    return render (request, 'store/items_view.html', context)

