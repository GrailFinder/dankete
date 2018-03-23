from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from ankete.models import Inquiry, Question
from ankete.api.serializers import InquirySerializer, UserSerializer

# inquiries
class InquiryListView(ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class InquiryRetrieveView(RetrieveAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

# questions
class QuestionListView(ListAPIView):
    queryset = Question.objects.all()

# users
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

