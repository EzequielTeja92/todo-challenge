
# Create your tests here.
from django.test import TestCase
from tasks.models import Task, Label
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TaskModelTest(TestCase):
    def setUp(self):
        self.label1 = Label.objects.create(name="Personal")
        self.label2 = Label.objects.create(name="Work")
        self.parent_task = Task.objects.create(
            title="Parent Task",
            description="Description for Parent Task",
            status="to-do",
            priority="medium"
        )
        self.child_task = Task.objects.create(
            title="Child Task",
            description="Description for Child Task",
            status="to-do",
            priority="medium",
            parent_task=self.parent_task
        )
        self.child_task.labels.add(self.label1, self.label2)

    def test_task_creation(self):
        self.assertEqual(self.parent_task.title, "Parent Task")
        self.assertEqual(self.child_task.parent_task, self.parent_task)
        self.assertEqual(self.child_task.labels.count(), 2)

    def test_task_string_representation(self):
        self.assertEqual(str(self.parent_task), self.parent_task.title)
