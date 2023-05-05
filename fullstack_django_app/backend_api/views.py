from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from .models import ContactMessage
from django.views.decorators.csrf import csrf_exempt
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


@method_decorator(csrf_exempt, name='dispatch')
class SaveContactMessageView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        return JsonResponse({"message": "Contact message saved successfully."})
