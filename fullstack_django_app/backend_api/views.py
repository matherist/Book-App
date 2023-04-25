from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
# Create your views here.
class BookView(APIView):
    def get(self, request):
        output =[{
            'title': output.title,
            'description': output.description,
            'link': output.link,
            'cost': output.cost

        } for output in Book.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer = Book(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
