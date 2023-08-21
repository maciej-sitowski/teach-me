from random import choice

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from questions.api.serializers import CategorySerializer, QuestionSerializer
from questions.models import Category, Question


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated, )


    @action(detail=False, methods=["GET"], url_path='get_random', url_name='get_random')
    def get_random(self, request):
        pks = Question.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        question = Question.objects.get(pk=random_pk)
        return Response(self.serializer_class(question).data, status=status.HTTP_200_OK)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
