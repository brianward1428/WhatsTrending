from django.contrib import admin

# Register your models here.
from scraping.models import ProductHuntElement, YouTubeElement, GoogleSearchElement, RedditGrowthElement, RedditActivityElement, RedditSubscribersElement
admin.site.register(ProductHuntElement)
admin.site.register(YouTubeElement)
admin.site.register(GoogleSearchElement)

admin.site.register(RedditGrowthElement)
admin.site.register(RedditActivityElement)
admin.site.register(RedditSubscribersElement)
