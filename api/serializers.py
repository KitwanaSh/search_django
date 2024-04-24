from rest_framework import serializers
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_score(self, obj):
        return obj.score