from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import Productserializers


class ProductViewModel(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializers
