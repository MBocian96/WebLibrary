from django.test import TestCase

from library.management.commands.load_books import BOOKS, Command as BookCommand
from library.models import Book


class CommandsHandlersTest(TestCase):
    def setUp(self):
        BookCommand().handle(options={BOOKS: 'data/ksiazki.csv'})

        def test_necessery_opinions_data_loaded_to_db(self):
            test_opinion_formatted = repr(Book.objects.get(pk=1))
            expected_opinion_content = '9788366436572, Stażystka, Alicja Sinicka, Kryminał'
            self.assertEqual(expected_opinion_content, test_opinion_formatted)
