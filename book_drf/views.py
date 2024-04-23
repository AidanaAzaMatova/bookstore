from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from book_drf.serializer import SerializerBookShop
from .models import BookShop

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.
def index(request):
    return render(
        request,
        'common/index.html',
        context={
        }
    )

class ListInfo(APIView):
    def get(self, request, format=None):
        article_titles = [article for article in BookShop.objects.all()]
        serializer = SerializerBookShop(article_titles, many=True)
        return Response(serializer.data)

class ModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = BookShop.objects.all()
    serializer_class = SerializerBookShop
