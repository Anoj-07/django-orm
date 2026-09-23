from rest_framework import serializers
from apps.models import Product, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__" 

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Product
        fields = "__all__" 
