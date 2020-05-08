from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)
    tags = serializers.ListField(write_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'body',
            'description',
            'slug',
            'title',
            'tags',
            'created_at',
            'updated_at'
        )
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])

        article = Article.objects.create(**validated_data)

        for tag in tags:
            article.tags.add(tag)

        return article
