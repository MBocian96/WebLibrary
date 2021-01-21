from rest_framework.test import APITestCase


class BookTests(APITestCase):

    def test_book_response(self):
        response = self.client.get('/api/v1/books/1')
        self.assertEqual(response.data, {
            "isnb": "9788366436572",
            "title": "Stażystka",
            "author": "Alicja Sinicka",
            "genre": "Kryminał"
        })
