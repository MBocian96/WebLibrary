from rest_framework import serializers

from library import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('isnb', 'title', 'author', 'genre',)


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Opinion
        fields = ('mark', 'description')
