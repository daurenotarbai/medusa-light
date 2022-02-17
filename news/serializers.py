from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Article
        fields = ["id", "subject", "content", "date"]
