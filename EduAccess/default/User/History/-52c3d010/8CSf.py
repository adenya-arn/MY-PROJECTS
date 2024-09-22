from django.shortcuts import render
from .models import Store, Items
# Create your views here.


def subjects_view(request, *args, **kwargs):
    stores = Store.objects.all()

    context = {'stores':stores}

    return render (request, 'store/store_view.html', context)


def subjects_view(request, *args, **kwargs):
    item = Items.objects.all()

    context = {'item':item}

    return render (request, 'store/items_view.html', context)

