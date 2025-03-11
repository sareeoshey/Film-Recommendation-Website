from django.shortcuts import render, redirect

# Create your views here.
# code I wrote
from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(watched=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', 
        {'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':#if form has been submitted
        form = SignupForm(request.POST) #all of the info in form

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })