from django.db import models


class Task(models.Model):
    IN_PROGRESS = 'In-Progress'
    DONE = 'Done'

    task_choices = [
        (IN_PROGRESS, 'In-Progress'),
        (DONE, 'Done')
    ]

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=12, choices=task_choices, default=IN_PROGRESS)
