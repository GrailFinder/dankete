from django.test import TestCase
from ankete.models import Inquiry
from django.contrib.auth.models import User
from django.urls import resolve


class InquiryTestCase(TestCase):
    def setUp(self):
        #user = User.objects.create(user="grail", email="grail@test.com", password="test")
        Inquiry.objects.create(title="test one", description="to test")

    def test_inq(self):
        inq = Inquiry.objects.get(title="test one")
        self.assertEqual(inq.description, "to test")

    def test_root_url_home_page(self):
        home_dict = {"users": "http://localhost:8000/api/users/", "inquiries": "http://localhost:8000/api/inqs/"}
        home_dict = {key: value.replace("localhost:8000", "testserver") for key, value in home_dict.items()}
        resp = self.client.get("/")
        data = resp.data
        print(data)
        self.assertEqual(home_dict, data)
