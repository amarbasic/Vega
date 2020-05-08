from django.db import models

from vega.common.models import BaseModel


class Article(BaseModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    tags = models.ManyToManyField('articles.Tag', through='ArticleTag')


class Comment(BaseModel):
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )


class Tag(BaseModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)



class ArticleTag(BaseModel):
    article = models.ForeignKey(
        'articles.Article', on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        'articles.Tag', on_delete=models.CASCADE
    )
