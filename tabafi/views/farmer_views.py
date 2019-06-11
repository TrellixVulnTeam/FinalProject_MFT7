from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from tabafi.models import Farmer, Product
from tabafi.serializers import FarmerSerializer, FarmerProductsSerializer, NewProductsSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_farmer(request, pk):
    try:
        farmer = Farmer.objects.get(pk=pk)
    except Farmer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single farmer
    if request.method == 'GET':
        if farmer.token == request.META['HTTP_AUTHORIZATION']:
            serializer = FarmerSerializer(farmer)
            return Response(serializer.data)
        else:
            return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)


    # delete a single farmer
    elif request.method == 'DELETE':
        farmer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single farmer
    elif request.method == 'PUT':
        serializer = FarmerSerializer(farmer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_farmers(request):
    if request.method == 'GET':
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)
    # insert a new record for a farmer
    elif request.method == 'POST':
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'phone_number': request.data.get('phone_number')
        }
        serializer = FarmerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_products(request, pk):
    farmer = Farmer.objects.get(pk=pk)
    if request.method == 'GET':
        farmer_token = request.META['HTTP_AUTHORIZATION']
        if farmer.token == farmer_token:
            products = Product.objects.all().filter(farmer=farmer)
            # print(products)
            serializer = FarmerProductsSerializer(instance=farmer)
            return Response(serializer.data)
        else:
            return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)
    # insert a new record for a farmer
    elif request.method == 'POST':
        data = {
            'farmer': int(pk),
            'fruit_name': request.data.get('fruit_name'),
            'weight': request.data.get('weight'),
            'price': request.data.get('price'),
            'description': request.data.get('description')
        }
        serializer = NewProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)