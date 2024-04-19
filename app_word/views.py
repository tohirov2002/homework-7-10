from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import OriginSerializer, CategorySerializer, WordSerializer
from .models import Origin, Category, Word


class OriginListView(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class WordListView(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
