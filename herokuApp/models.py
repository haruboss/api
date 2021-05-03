from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.titile
