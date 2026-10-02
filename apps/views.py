from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.models import Product
from apps.serializer import ProductSerializer


# TO AVOID N + 1 Query => user select_related and prefech related
class ProductView(APIView):
    def get(self, request):
        # qs = Product.objects.filter(is_active=True)
        qs = Product.objects.filter(is_active=True).select_related("company")
        serializer = ProductSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
