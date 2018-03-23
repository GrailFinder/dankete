from django.db import models
from django.contrib.auth.models import User
import uuid, datetime


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Answer(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    text = models.TextField(null=False)
    value = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=False, auto_now=True)


    def __str__(self):
        return f'{self.title}: {self.id}'

class Question(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    title = models.TextField(null=False)
    created_at = models.DateTimeField(null=False, auto_now=True)
    multiansw = models.BooleanField(default=False)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return f'{self.title}: {self.id}'


class Inquiry(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    title = models.TextField(null=False)
    created_at = models.DateTimeField(null=False, auto_now=True)
    description = models.TextField(null=True)
    questions = models.ManyToManyField(Question)
    owner = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.title}: {self.id}'