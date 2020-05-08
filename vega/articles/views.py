from rest_framework.viewsets import ModelViewSet

from .serializers import ArticleSerializer
from .models import Article


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = []
