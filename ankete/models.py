from django.db import models
from django.contrib.auth.models import User
import uuid, datetime


class Answer(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    choice_id = models.ForeignKey('Choice', on_delete=models.CASCADE)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    inqiury_id = models.ForeignKey('Inquiry', on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, auto_now=True)


class Choice(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    text = models.TextField(null=False)
    value = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, auto_now=True)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return f'{self.text}: {self.id}'


class Question(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    title = models.TextField(null=False)
    created_at = models.DateTimeField(null=False, auto_now=True)
    multiansw = models.BooleanField(default=False)
    inqiury_id = models.ForeignKey('Inquiry', on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return f'{self.title}: {self.id}'


class Inquiry(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    title = models.TextField(null=False)
    created_at = models.DateTimeField(null=False, auto_now=True)
    description = models.TextField(null=True)
    owner = models.ForeignKey(User, related_name='inquiries', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.id}'