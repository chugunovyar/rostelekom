from django.test import TestCase
from django.test import Client

from main import settings


class TestMainPage(TestCase):

    def setUp(self):
        self.c = Client()
        settings.ROOT_URLCONF=__name__

    def tearDown(self):
        pass

    def test_index_page(self):
        resp = self.c.get("/")
        self.assertEqual(resp.status_code, 200)
