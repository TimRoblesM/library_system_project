from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

