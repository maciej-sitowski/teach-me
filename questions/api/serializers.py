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
