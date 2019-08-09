from rest_framework import serializers
from .models import Farmer, Customer, Product, Request, ProductImage


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'phone_number', 'created_at', 'updated_at')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'phone_number', 'created_at', 'updated_at')


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'username', 'first_name', 'last_name', 'shop_name', 'token')


class FarmerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'username', 'first_name', 'last_name', 'token')


class ProductFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'first_name', 'last_name', 'username', 'phone_number')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image_file')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    farmer = ProductFarmerSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'farmer', 'fruit_name', 'weight', 'price', 'description', 'farm_lat', 'farm_lng', 'province', 'city',
            'address', 'created_at', 'updated_at', 'images')


class FarmerProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Farmer
        # fields = ('id', 'products')
        fields = ('id', 'username', 'products')


class RequestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'username', 'phone_number')


class RequestSerializer(serializers.ModelSerializer):
    customer = RequestUserSerializer(many=False, read_only=True)

    class Meta:
        model = Request
        fields = (
            'id', 'customer', 'fruit_name', 'weight', 'description', 'customer_lat', 'customer_lng', 'province', 'city',
            'address', 'created_at', 'updated_at')
