from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Loan
from .serializers import LoanSerializer

class LoanListAPIView(APIView):
    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)