from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from tabafi.models import Customer
from tabafi.serializers import CustomerSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single customer
    if request.method == 'GET':
        if request.method == 'GET':
            if customer.token == request.META['HTTP_AUTHORIZATION']:
                serializer = CustomerSerializer(customer)
                return Response(serializer.data)
            else:
                return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)

    # delete a single customer
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single customer
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    # insert a new record for a customer
    elif request.method == 'POST':
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'username': request.data.get('username'),
            'shop_name': request.data.get('shop_name'),
            'phone_number': request.data.get('phone_number')
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)