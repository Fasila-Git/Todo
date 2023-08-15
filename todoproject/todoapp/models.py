from django.db import models

# Create your models here.
class Task(models.Model):
    taskName=models.CharField(max_length=200)
    taskPriority=models.IntegerField()
    taskDate=models.DateField()

    def __str__(self):
        return self.taskName