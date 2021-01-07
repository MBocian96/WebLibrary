from django.core.management import call_command
from django.test import TestCase

from library.models import Book, Opinion


class CommandsHandlersTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CommandsHandlersTest, cls).setUpClass()
        call_command('load_books', 'library/tests/data/ksiazki.csv')
        call_command('load_opinions', 'library/tests/data/opinie.csv')

    def test_book_data_loaded_to_db(self):
        test_opinion_formatted = repr(Book.objects.get(pk=1))
        expected_opinion_content = '9788366436572, Stażystka, Alicja Sinicka, Kryminał'
        self.assertEqual(expected_opinion_content, test_opinion_formatted)

    def test_opinions_data_loaded_to_db(self):
        test_opinion_formatted = repr(Opinion.objects.get(pk=1))
        expected_opinion_content = '4, test1'
        self.assertEqual(expected_opinion_content, test_opinion_formatted)
