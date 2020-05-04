from vega.common.tests import BasetTestCase

from vega.articles.models import Article


class ArticlesTestCase(BasetTestCase):

    def test_should_create_article(self):
        article = Article(
            slug='my-article',
            title='My article',
            body='Hello World!',
            description='My first article'
        )

        article.save()

        self.assertIsNotNone(article.pk)
        self.assertIsNotNone(article.slug)
