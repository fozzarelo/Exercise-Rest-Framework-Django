from rest_framework import generics
from goals.models import Goal, Task
from goals.serializers import GoalSerializer, TaskSerializer


class ListCreateGoals(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class ListCreateTasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
