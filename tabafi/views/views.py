import binascii
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tabafi.models import Farmer, Customer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        # data = {
        #     'username': request.data.get('username'),
        #     'password': request.data.get('password'),
        #     'user_type': request.data.get('user_type'),
        # }
        if request.data.get('username') is None or request.data.get('password') is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        elif request.data.get('user_type') == '0':
            customers = Customer.objects.all()
            for customer in customers:
                if request.data.get('username') == customer.username:
                    token = binascii.hexlify(os.urandom(20)).decode()
                    customer.token = token
                    customer.save()
                    return Response({'token': customer.token, 'id': customer.id, 'name': customer.first_name},
                                    status=status.HTTP_200_OK)
        elif request.data.get('user_type') == '1':
            farmers = Farmer.objects.all()
            for farmer in farmers:
                if request.data.get('username') == farmer.username:
                    token = binascii.hexlify(os.urandom(20)).decode()
                    farmer.token = token
                    farmer.save()
                    return Response({'token': farmer.token, 'id': farmer.id, 'name': farmer.first_name},
                                    status=status.HTTP_200_OK)
        return Response({'error': 'user not found'}, status=status.HTTP_401_UNAUTHORIZED)
