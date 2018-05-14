from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from ankete.models import Inquiry, Question, Choice
from rest_framework import serializers

class InquirySerializer(ModelSerializer):
    questions = PrimaryKeyRelatedField(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Inquiry
        fields = [
            'id',
            'title',
            'created_at',
            'description',
            'questions',
            'owner',
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',
        'email', 'date_joined', 'last_login']

class QuestionSerializer(ModelSerializer):
    answers = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id',
            'title',
            'created_at',
            'multiansw',
            'answers',
            ]

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id',
        'text',
        'created_at',
        'value',
        ]

class AnswerSerializer(ModelSerializer):
    class Meta:
        fields = [
            'id',
            'choice_id',
            'question_id',
            'inqiury_id',
            'created_at',
        ]