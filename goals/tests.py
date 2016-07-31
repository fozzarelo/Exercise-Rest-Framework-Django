from goals.models import Task, Goal
from rest_framework.test import APITestCase

class GetGoalsTest(APITestCase):

    def setUp(self):
        self.client.post('/api/goals', {'name': 'Goal Test1'})
        self.client.post('/api/goals', {'name': 'Goal Test2'})
        self.response = self.client.get('/api/goals')

    def test_get_goals_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_goals_content(self):
        self.assertContains(self.response, 'Goal Test1')
        self.assertContains(self.response, 'Goal Test2')


class GetTasksTest(APITestCase):

    def setUp(self):
        self.client.post('/api/tasks', {'name': 'Task Test1'})
        self.client.post('/api/tasks', {'name': 'Task Test2'})
        self.response = self.client.get('/api/tasks')

    def test_get_goals_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_goals_content(self):
        self.assertContains(self.response, 'Task Test1')
        self.assertContains(self.response, 'Task Test2')


class PostGoalsWithTasksTest(APITestCase):

    def setUp(self):
        self.tasks_b4_post = Task.objects.count()
        self.goals_b4_post = Goal.objects.count()

    def test_post_goals_with_tasks(self):
        self.client.post('/api/goals',
                         {"name": "Test Goal", "tasks": [{"name": "Test task 1"}, {"name": "Test task 2"}]},
                         format='json')
        self.assertEquals(Goal.objects.count(), self.goals_b4_post + 1)
        self.assertEquals(Task.objects.count(), self.tasks_b4_post + 2)

