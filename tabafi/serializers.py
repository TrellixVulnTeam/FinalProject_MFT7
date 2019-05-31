from rest_framework import serializers
from .models import Farmer, Customer


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
