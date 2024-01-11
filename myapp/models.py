from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hobbies = models.CharField(max_length=100, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
