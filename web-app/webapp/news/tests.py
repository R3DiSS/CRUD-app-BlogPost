from django.test import TestCase
from .models import Articles  

class ArticlesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Articles.objects.create(title='Test Title', anons='Test Anons', full_text='Test Body', date='2023-09-16T00:00')

    def test_news_home_view(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_news_detail_view(self):
        article = Articles.objects.get(id=1)
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_news_create_view(self):
        response = self.client.get('/news/create')
        self.assertEqual(response.status_code, 200)
    

