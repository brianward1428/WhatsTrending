from django.urls import include, path
from rest_framework import routers
from . import views

'''
Initialize routers
'''
router_ProductHuntElement = routers.DefaultRouter()
router_ProductHuntElement.register(r'ProductHuntElement', views.ProductHuntElementViewSet)

router_GoogleSearchElement = routers.DefaultRouter()
router_GoogleSearchElement.register(r'GoogleSearchElement', views.GoogleSearchElementViewSet)

router_YouTubeElement = routers.DefaultRouter()
router_YouTubeElement.register(r'YouTubeElement', views.YouTubeElementViewSet)

router_RedditGrowthElement = routers.DefaultRouter()
router_RedditGrowthElement.register(r'RedditGrowthElement', views.RedditGrowthElementViewSet)

router_RedditActivityElement = routers.DefaultRouter()
router_RedditActivityElement.register(r'RedditActivityElement', views.RedditActivityElementViewSet)

router_RedditSubscribersElement = routers.DefaultRouter()
router_RedditSubscribersElement.register(r'RedditSubscribersElement', views.RedditSubscribersElementViewSet)


'''
Set up URLS
'''
urlpatterns = [
	path('', views.home, name='home'),
    path('api/ProductHuntElement/', include(router_ProductHuntElement.urls)),
	path('api/YouTubeElement/', include(router_YouTubeElement.urls)),
	path('api/GoogleSearchElement/', include(router_GoogleSearchElement.urls)),
	path('api/RedditGrowthElement/', include(router_RedditGrowthElement.urls)),
	path('api/RedditActivityElement/', include(router_RedditActivityElement.urls)),
	path('api/RedditSubscribersElement/', include(router_RedditSubscribersElement.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
