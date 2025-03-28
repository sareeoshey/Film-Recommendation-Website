from django.shortcuts import render, get_object_or_404, redirect
# I added get_object_or_404

# Create your views here.
# I wrote code below

from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm, EditItemForm


def items(request):
    items = Item.objects.filter(watched=False)
    watched_items = Item.objects.filter(watched=True)

    return render(request, 'item/items.html', {
        'items': items,
        'watched_items': watched_items,
    })

def detail(request, pk):#primary key
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, watched=False).exclude(pk=pk)[0:3]
    # related_watched = Item.objects.filter(category=item.category, watched=True).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False) #we have to create object first then save to data base
            item.created_by = request.user
            item.user()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):#pk which is id for item we want to delete
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
