from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Item, List

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        text = request.POST.get('item_text', '')
        list_ = List.objects.create()
        Item.objects.create(text=text, list=list_)
        return redirect('/lists/%d/' % (list_.id, ))
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        item = Item(text=request.POST['item_text'], list=list_)
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            error = "You can't have an empty list item"
            return render(request, 'list.html', {'list': list_, 'error': error})
            #return redirect('/lists/%d/' % (list_.id,), error=error)
        return redirect('/lists/%d/' % (list_.id,))
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    error = None
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = 'You can\'t have an empty list item'
    return render(request, 'home.html', {'error': error})

def add_item(request, list_id):
    if request.method == 'POST':
        list_ = List.objects.get(id=list_id)
        item = Item(list=list_, text=request.POST['item_text'])
        #Item.objects.create(text=request.POST['item_text'], list=list_)
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            error = "You can't have an empty list item"
            return render(request, 'list.html', {'list': list_, 'error': error})
            #return redirect('/lists/%d/' % (list_.id,), error=error)
        return redirect('/lists/%d/' % (list_.id,))
    else:
        return redirect('/lists/%d/' % (list_.id,))





