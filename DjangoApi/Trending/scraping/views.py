from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class ProductHuntElementViewSet(viewsets.ModelViewSet):
    queryset = models.ProductHuntElement.objects.all()
    serializer_class = serializers.ProductHuntElementSerializer

class YouTubeElementViewSet(viewsets.ModelViewSet):
    queryset = models.YouTubeElement.objects.all()
    serializer_class = serializers.YouTubeElementSerializer

class GoogleSearchElementViewSet(viewsets.ModelViewSet):
    queryset = models.GoogleSearchElement.objects.all()
    serializer_class = serializers.GoogleSearchElementSerializer

class RedditGrowthElementViewSet(viewsets.ModelViewSet):
    queryset = models.RedditGrowthElement.objects.all()
    serializer_class = serializers.RedditGrowthElementSerializer

class RedditActivityElementViewSet(viewsets.ModelViewSet):
    queryset = models.RedditActivityElement.objects.all()
    serializer_class = serializers.RedditActivityElementSerializer

class RedditSubscribersElementViewSet(viewsets.ModelViewSet):
    queryset = models.RedditSubscribersElement.objects.all()
    serializer_class = serializers.RedditSubscribersElementSerializer


def home(request):

    return render(request, 'scraping/home.html')
