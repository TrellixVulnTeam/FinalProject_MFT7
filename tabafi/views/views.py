import binascii
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tabafi.models import Farmer, Customer
from django.views.decorators.csrf import csrf_exempt

from tabafi.serializers import CustomerLoginSerializer, FarmerLoginSerializer


@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        if request.data.get('username') is None or request.data.get('password') is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        elif request.data.get('user_type') == '0':
            customers = Customer.objects.all()
            for customer in customers:
                if request.data.get('username') == customer.username and request.data.get('password') == customer.password:
                    token = binascii.hexlify(os.urandom(20)).decode()
                    customer.token = token
                    customer.save()
                    serializer = CustomerLoginSerializer(customer)
                    return Response(serializer.data,
                                    status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'wrong username or password'},
                                    status=status.HTTP_401_UNAUTHORIZED)
        elif request.data.get('user_type') == '1':
            farmers = Farmer.objects.all()
            for farmer in farmers:
                if request.data.get('username') == farmer.username  and request.data.get('password') == farmer.password:
                    token = binascii.hexlify(os.urandom(20)).decode()
                    farmer.token = token
                    farmer.save()
                    serializer = FarmerLoginSerializer(farmer)
                    return Response(serializer.data,
                                    status=status.HTTP_200_OK)
            else:
                return Response({'error': 'wrong username or password'},
                                status=status.HTTP_401_UNAUTHORIZED)
        # return Response({'error': 'user not found'}, status=status.HTTP_401_UNAUTHORIZED)
