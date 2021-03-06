"""ankete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ankete.api.views import (InquiryListView, QuestionListView, UserListView,
 InquiryRetrieveView, UserRetrieveView, ChoiceListView, AnswerListView)
from ankete.views import ping
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework_swagger.views import get_swagger_view
from .views import api_root, InquiryHighlight

schema_view = get_swagger_view(title='Ankete API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^ping/$', ping),
    url(r'^docs/$', schema_view),

    url(r'^api/inqs/$', InquiryListView.as_view(), name="inquiry-list"),
    url(r'^api/inqs/(?P<pk>[0-9a-f-]+)/$', InquiryRetrieveView.as_view(), name="inquiry"),
    url(r'^api/quests/$', QuestionListView.as_view(), name="question-list"),
    url(r'^api/choices/$', ChoiceListView.as_view(), name="choice-list"),
    url(r'^api/answers/$', AnswerListView.as_view(), name="answer-list"),
    url(r'^api/users/$', UserListView.as_view(), name="user-list"),
    url(r'^api/users/(?P<pk>[0-9a-f-]+)/$', UserRetrieveView.as_view(), name="user"),

    
    url(r'^$', api_root),
    url(r'^inqs/(?P<pk>[0-9]+)/highlight/$', InquiryHighlight.as_view()),
]

urlpatterns += staticfiles_urlpatterns()  # https://stackoverflow.com/questions/12800862/how-to-make-django-serve-static-files-with-gunicorn
