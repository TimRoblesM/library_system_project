from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    book_name = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = Loan
        fields = (
            'id',
            'user',
            'user_name',
            'book',
            'book_name',
            'loan_date',
            'return_date',
        )