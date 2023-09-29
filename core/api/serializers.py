from core.models import Product
from rest_framework import serializers

class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductGetSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Product
        fields = "__all__"


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"