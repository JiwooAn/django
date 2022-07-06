from django.test import TestCase
from django.urls import resolve
from .views import index


# Create your tests here.
class PyboPageTest(TestCase):
    def test_pybo_url_resolves_to_pybo_page_view(self):
        found = resolve('/pybo/')
        self.assertEqual(found.func, index)

