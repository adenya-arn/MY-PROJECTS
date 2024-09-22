from django.shortcuts import render
from .models import Store, Items
# Create your views here.


def subjects_view(request, *args, **kwargs):
    stores = Store.objects.all()

    context = {'stores':stores}

    return render (request, 'store/store_view.html', context)
def subjects_view(request, *args, **kwargs):
    subject = Subjects.objects.all()

    context = {}

    return render (request, 'school/subjects_view.html', context)

