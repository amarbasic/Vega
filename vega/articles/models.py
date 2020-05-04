from django.db import models

from vega.common.models import TimestampedMixin


class Article(TimestampedMixin):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    tags = models.ManyToManyField('articles.Tag', through='ArticleTag')


class Comment(TimestampedMixin):
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )


class Tag(TimestampedMixin):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)



class ArticleTag(TimestampedMixin):
    article = models.ForeignKey(
        'articles.Article', on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        'articles.Tag', on_delete=models.CASCADE
    )
