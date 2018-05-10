from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from ankete.models import Inquiry, Question, Answer

class InquirySerializer(ModelSerializer):
    questions = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Inquiry
        fields = [
            'id',
            'title',
            'created_at',
            'description',
            'questions',
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',
        'email', 'date_joined', 'last_login']

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title',
        'created_at', 'multiansw',]

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'created_at',
        'value']