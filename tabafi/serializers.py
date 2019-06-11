from rest_framework import serializers
from .models import Farmer, Customer, Product


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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('farmer', 'fruit_name', 'weight', 'price', 'description')


class FarmerProductsSerializer(serializers.ModelSerializer):
    print('here1')
    products = ProductSerializer(many=True, read_only=True)
    print('here2')

    class Meta:
        model = Farmer
        fields = ('id', 'username', 'products')


class NewProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('farmer', 'fruit_name', 'weight', 'price', 'description')
