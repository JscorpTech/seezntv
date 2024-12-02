from rest_framework import serializers

from core.apps.content.models.category import CategoryList


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = "__all__"
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=250)
