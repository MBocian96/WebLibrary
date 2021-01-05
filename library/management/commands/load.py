from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load books and their opinions in csv files'

    def add_arguments(self, parser):
        parser.add_argument('load', nargs='+', type=str)

    def handle(self, *args, **options):
        pass
