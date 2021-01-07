# Create your models here.
from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE


class Book(models.Model):
    isnb = CharField(max_length=13)
    title = CharField(max_length=40)
    author = CharField(max_length=40)
    genre = CharField(max_length=40)

    def __repr__(self):
        return f'{self.isnb}, {self.title}, {self.author}, {self.genre}'


class Opinion(models.Model):
    isnb = CharField(max_length=13)
    mark = IntegerField(default=0)
    description = CharField(max_length=50)

    book = ForeignKey(Book, on_delete=CASCADE)

    def __repr__(self):
        return f'{self.mark}, {self.description}'
