from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.store.models import Products, Services, Policy
from .serializer import ProductSerializer, ServicesSerializer, PolicySerializer


class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class ServicesView(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()


class PolicyView(viewsets.ModelViewSet):
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()


@api_view(['GET'])
def getProducts(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
