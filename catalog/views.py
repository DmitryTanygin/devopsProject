from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    return render(request, 'index.html',
                  context={'num_books': num_books, 'num_instance': num_instances,
                           'num_instance_available': num_instances_available,
                           'num_authors': num_authors},
                  )
