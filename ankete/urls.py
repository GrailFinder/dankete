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
from django.conf.urls import url
from django.contrib import admin
from ankete.api.views import InquiryListView, QuestionListView, UserListView, InquiryRetrieveView
from ankete.views import ping

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ping/$', ping),
    url(r'^api/inquiries/$', InquiryListView.as_view(), name="inquiry_list"),
    url(r'^api/inquiry/(?P<pk>[0-9a-f-]+)/$', InquiryRetrieveView.as_view(), name="inquiry"),
    url(r'^api/users/$', UserListView.as_view(), name="user_list"),
]
