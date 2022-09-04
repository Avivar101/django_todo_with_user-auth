from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    user = models.ForeignKey(
        # in case a user is deleted all its created task should be deleted from the db
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
