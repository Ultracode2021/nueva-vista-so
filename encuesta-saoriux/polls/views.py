from .serializers import QuestionSerializer
from rest_framework import viewsets
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer