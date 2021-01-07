import csv

from django.core.management.base import BaseCommand

from library.models import Book

BOOKS = 'books'


class Command(BaseCommand):
    help = 'Load books and their opinions'

    def add_arguments(self, parser):
        parser.add_argument(BOOKS, nargs='+', type=str)

    def handle(self, *args, **options):
        books_csv_paths = options[BOOKS]
        for csv_file_path in books_csv_paths:
            with open(csv_file_path, mode='r', encoding='UTF-8', newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                next(csv_reader, None)
                for row in csv_reader:
                    new_book = Book(isnb=row[0], title=row[1], author=row[2], genre=row[3])
                    try:
                        new_book.save()
                    except ValueError as v_err:
                        self.stdout.write(self.style.ERROR(f'Book{row[1]} can not be saved'))
        self.stdout.write(self.style.SUCCESS('Books successfully loaded'))
