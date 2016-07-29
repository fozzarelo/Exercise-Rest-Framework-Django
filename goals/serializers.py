from rest_framework import serializers
from goals.models import Goal, Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'goal')


class GoalSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Goal
        fields = ('name', 'description', 'tasks')

    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks')
        goal = Goal.objects.create(**validated_data)
        for task_item in tasks_data:
            Task.objects.create(name=task_item["name"], goal=goal)
        return goal

