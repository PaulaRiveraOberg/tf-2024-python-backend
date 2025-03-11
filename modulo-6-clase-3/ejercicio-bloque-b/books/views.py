from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BibliotecaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.filter(is_exclusive=False)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class SalaVIPAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        books = Book.objects.filter(is_exclusive=True)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
