from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('to-do', 'To-do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to-do')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    labels = models.ManyToManyField(Label, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)

    def __str__(self):
        return self.title