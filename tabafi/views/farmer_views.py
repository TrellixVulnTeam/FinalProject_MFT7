from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from tabafi.models import Farmer
from tabafi.serializers import FarmerSerializer


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