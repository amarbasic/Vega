from django.urls import reverse
from rest_framework import status

from vega.common.tests import APITestCase
from vega.articles.models import Article, Tag


class ArticleAPITestCase(APITestCase):
    def test_should_create_article_with_tags(self):
        tag = Tag.objects.create(tag='article', slug='article')
        request_body = {
            'title': 'Test article',
            'body': 'Article body',
            'tags': [tag.pk]
        }

        url = reverse('articles:article-list')
        response = self.client.post(url, request_body)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        article = Article.objects.get(pk=response_data['id'])
        self.assertEqual(article.tags.count(), len(request_body['tags']))
