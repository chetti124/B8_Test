from .models import Product

from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"