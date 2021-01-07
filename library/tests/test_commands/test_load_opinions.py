from django.test import TestCase

from library.management.commands.load_opinions import OPINIONS, Command as OpinionCommand
from library.models import Opinion


class CommandsHandlersTest(TestCase):
    def setUp(self):
        OpinionCommand().handle(options={OPINIONS: 'data/opinie.csv'})

    def test_necessery_opinions_data_loaded_to_db(self):
        test_opinion_formatted = repr(Opinion.objects.get(pk=1))
        expected_opinion_content = '9788366436572, 4, test1'
        self.assertEqual(expected_opinion_content, test_opinion_formatted)
