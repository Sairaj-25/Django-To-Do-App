from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # Task title
    title = models.CharField(max_length=255,help_text="enter task title")

    # Description
    description = models.TextField(help_text="enter task details")

    # Due Date
    due_date = models.DateField(help_text="enter deadline of task")

    # time of creation
    create_time = models.DateTimeField(help_text="task is created at")

    # time of edit
    edit_time = models.DateTimeField(help_text="task is edited at",blank=True,null=True)

    # Associate each task with user
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title