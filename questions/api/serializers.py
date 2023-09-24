from rest_framework import serializers
from ..models import Category, Question


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class QuestionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Question
        fields = ['id', 'title', 'answer', 'category_name']

    def create(self, validated_data):
        category = Category.objects.get(name=validated_data['category']['name'])
        validated_data['category'] = category
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "category" in validated_data:
            category = Category.objects.get(name=validated_data['category']['name'])
            validated_data['category'] = category

        return super().update(instance, validated_data)
