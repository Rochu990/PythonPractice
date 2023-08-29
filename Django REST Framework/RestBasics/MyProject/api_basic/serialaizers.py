from rest_framework import serializers
from .models import Article


class ArticleSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']
        