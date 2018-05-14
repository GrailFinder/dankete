from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.contrib.auth.models import User
from ankete.models import Inquiry, Question, Choice, Answer
from ankete.api.serializers import InquirySerializer, UserSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
from ankete.api.permissions import IsOwnerOrReadOnly


# inquiries
class InquiryListView(ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.reques.user)

class InquiryRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# questions
class QuestionListView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# choices
class ChoiceListView(ListAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# answers
class AnswerListView(ListAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# users
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = InquirySerializer