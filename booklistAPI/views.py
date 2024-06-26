from django.db import IntegrityError
from rest_framework.response import Response
from .models import Book
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict


# Create your views here.
@api_view(['GET', 'POST'])
# @csrf_exempt

def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return Response({"books":list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return Response({'error':'true','message':'required field missing'},status=400)

        return Response(model_to_dict(book), status=201)