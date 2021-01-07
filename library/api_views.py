from rest_framework import viewsets

from library import models, serializers


class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class OpinionViewset(viewsets.ModelViewSet):
    queryset = models.Opinion.objects.all()
    serializer_class = serializers.OpinionSerializer
