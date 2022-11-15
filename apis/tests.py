from django.urls import reverse
from books.models import Book
from rest_framework.test import APITestCase
from rest_framework import status

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title='Django for APIs',
            subtitle='Build web APIs with Python and Django',
            author='Kenneth Baah Danso',
            isbn='#009203000'
        )

    def test_api_listview(self):
        response=self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK) 
        self.assertAlmostEqual(Book.objects.count(),1)
        self.assertContains(response,self.book)   

