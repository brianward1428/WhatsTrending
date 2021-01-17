from rest_framework import serializers

from . import models
class ProductHuntElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductHuntElement
        fields = ('id', 'name', 'description', 'upvotes', 'link')

class GoogleSearchElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GoogleSearchElement
        fields = ('id', 'title', 'searchCount', 'link')

class YouTubeElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.YouTubeElement
        fields = ('id', 'title', 'info', 'link')

class RedditGrowthElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RedditGrowthElement
        fields = ('id', 'title', 'growth', 'link')

class RedditActivityElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RedditActivityElement
        fields = ('id', 'title', 'subscribers', 'link')

class RedditSubscribersElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RedditSubscribersElement
        fields = ('id', 'title', 'subscribers', 'link')
