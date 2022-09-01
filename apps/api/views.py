from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.store.models import Products, ProductReview
from .serializer import ProductSerializer


# from .products import products


@api_view(['GET'])
def getRoutes(request):
    routes = [
        "/api/products/",
        "/api/products/create",
        "/api/products/<update>/<id>",
        "/api/products/delete/<id>",
        "/api/products/upload",
        "/api/products/<:id>/reviews/",
        "/api/products/top",
        "/api/products/<:id>/",

    ]
    return Response(routes)


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


@api_view(['GET'])
def get_review_count(request, product_id):
    review_count = ProductReview.object.annotate(num_reviews=Count('product_id'))
    return Response(review_count)
