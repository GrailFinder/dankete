from django.test import TestCase
from ankete.models import Inquiry
from django.contrib.auth.models import User


class InquiryTestCase(TestCase):
    def setUp(self):
        #user = User.objects.create(user="grail", email="grail@test.com", password="test")
        Inquiry.objects.create(title="test one", description="to test")


    def test_inq(self):
        inq = Inquiry.objects.get(title="test one")
        self.assertEqual(inq.description, "to test")