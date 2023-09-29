from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from core.models import Product
from .serializers import ProductGetSerializer , ProductPostSerializer 


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all(is_published=True)
        serializer = ProductGetSerializer(products, many=True, context={'request': request})
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductPostSerializer(data=request.data , context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailApiView(APIView):
    def get(self, request, id):
        try:
            products = Product.objects.get(id=id)
            serializer = ProductGetSerializer(products, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND , data={'message': 'Product not found'})

    def put(self, request, id):
        try:
            products = Product.objects.get(id=id)
            serializer = ProductPostSerializer(products, data=request.data , context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND , data={'message': 'Product not found'})
        
    def delete(self, request, id):
        try:
            products = Product.objects.get(id=id)
            products.delete()
            return Response(status=status.HTTP_204_NO_CONTENT , data={'message': 'Product deleted'})
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND , data={'message': 'Product not found'})

