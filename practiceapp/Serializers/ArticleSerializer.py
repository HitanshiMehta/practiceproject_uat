from rest_framework import serializers

from practiceapp.models.ArticleModel import  Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self,instance,validate_data):
        instance.title=validate_data.get('title',instance.title)
        instance.description = validate_data.get('description', instance.description)
        instance.body = validate_data.get('body', instance.body)
        instance.save()
        return instance