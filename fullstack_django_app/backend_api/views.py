from django.shortcuts import render
from rest_framework.views import APIView
from .models import YouTube
from .serializer import YouTubeSerializer
from rest_framework.response import Response
# Create your views here.
class YouTubeView(APIView):
    def get(self, request):
        output =[{
            'title': output.title,
            'description': output.description,
            'link': output.link

        } for output in YouTube.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer = YouTubeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
