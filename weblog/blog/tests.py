from django.test import TestCase
from django.urls import resolve

from .views import index


class BlogTests(TestCase):
    def test_index_page_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_page_1_exists(self):
        response = self.client.get("/page/1")
        self.assertEqual(response.status_code, 200)

    def test_index_page_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/index.html")

    def test_index_page_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Writing Blogs Made Easy")

    def test_index_page_does_contain_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "I should not be on the page")

    def test_index_page_url_resolve_index_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, index.__name__)
