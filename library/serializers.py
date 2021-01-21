from rest_framework import serializers

from library import models
from library.models import Book, Opinion


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('isnb', 'title', 'author', 'genre',)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.isnb = validated_data.get('isnb', instance.isnb)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Opinion
        fields = ('mark', 'description')

    def create(self, validated_data):
        return Opinion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mark = validated_data.get('mark', instance.mark)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
