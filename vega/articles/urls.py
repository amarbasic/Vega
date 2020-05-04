from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet, 'article')


app_name = 'articles'

urlpatterns = [
    path('', include(router.urls), name='article'),
]
