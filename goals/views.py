from django.shortcuts import render
from rest_framework import generics
from goals.models import Goal
from goals.serializers import GoalSerializer


class ListCreateGoals(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

