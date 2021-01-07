import csv

from django.core.management.base import BaseCommand

from library.models import Book

OPINIONS = 'opinions'


class Command(BaseCommand):
    help = 'Load opinions'

    def add_arguments(self, parser):
        parser.add_argument(OPINIONS, nargs='+', type=str)

    def handle(self, *args, **options):
        opinions_csv_paths = options[OPINIONS]
        for csv_file_path in opinions_csv_paths:
            with open(csv_file_path, mode='r', encoding='UTF-8', newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                next(csv_reader, None)
                for row in csv_reader:
                    try:
                        b = Book.objects.get(isnb=row[0])
                        b.opinion_set.create(mark=row[1], description=row[2])
                    except Book.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f'Book does not exists'))
        print(self.stdout.write(self.style.SUCCESS('Opinions successfully loaded')))
