from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book
from library.serializers import BookSerializer


class BookList(APIView):
    def get(self, request, format=None):
        snippets = Book.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):
    def get_book(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_book(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_book(pk)
        book.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
