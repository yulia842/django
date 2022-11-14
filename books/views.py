from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from books.forms import BookForm
from books.models import Book


def books(request):
    my_books = Book.objects.all()
    context = {
       'book_list': my_books
    }
    return render(request,'books.html', context=context)


def add(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST , request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('books:list')  
    else:
        bookform = BookForm()
   
    context = {
        'bookform': bookform,
    }
    return render(request, "add_form.html", context=context)


def delete(request):
    return HttpResponse("DELETED")

def search(request):
    search = request.GET.get('search')
   
    my_books = Book.objects.filter(name__contains=search).values() | Book.objects.filter(author__contains=search).values()
    context = {
       'book_list': my_books
    }
    return render(request,'books.html', context=context)


