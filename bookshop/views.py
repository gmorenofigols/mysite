from django.shortcuts import render
from bookshop import models as m

# Create your views here.


def home(request):
    return render(request, 'home_user.html')


def books(request):
    all_books = m.Book.objects.all()
    return render(request, 'list_all.html', {'books': all_books})


def book_description(request, book_id):
    book = m.Book.objects.filter(id=book_id)
    return render(request, 'book.html', {'book': book})


def authors(request):
    all_authors = m.Author.objects.all()
    return render(request, 'list_all.html', {'authors': all_authors})


def author_description(request, author_id):
    author = m.Author.objects.filter(id=author_id)
    return render(request, 'author.html', {'author': author})
