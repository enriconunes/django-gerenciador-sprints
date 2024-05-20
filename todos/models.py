from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    project = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    createdAt = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finishedAt = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]