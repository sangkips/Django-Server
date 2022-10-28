from email.policy import default
from django.db import models

# Create your models here.
class Bio(models.Model):
    slackUsername = models.CharField(max_length=250)
    backend = models.BooleanField(default=False, null=True, blank=True)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername
