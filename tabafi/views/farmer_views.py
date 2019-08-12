from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from tabafi.models import Farmer, Product, ProductImage, Request, Customer
from tabafi.serializers import FarmerSerializer, FarmerProductsSerializer, ProductSerializer, ProductImageSerializer, \
    RequestSerializer


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
    try:
        farmer = Farmer.objects.get(pk=pk)
    except Farmer.DoesNotExist:
        return Response({'error': 'Farmer not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        if farmer.token == request.META['HTTP_AUTHORIZATION']:
            serializer = FarmerProductsSerializer(instance=farmer, context={'request': request})
            return Response(serializer.data)
        else:
            return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)
    # insert a new record for a farmer
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_product(request, uuid, pk):
    farmer = Farmer.objects.get(pk=uuid)
    try:
        if farmer.token == request.META['HTTP_AUTHORIZATION']:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status.HTTP_404_NOT_FOUND)

            # get details of a single product
            if request.method == 'GET':
                # images = ProductImage(product)
                serializer = ProductSerializer(product, context={'request': request})
                return Response(serializer.data)
                # if customer.token == request.META['HTTP_AUTHORIZATION']:
                #     serializer = CustomerSerializer(customer)
                #     return Response(serializer.data)
                # else:
                #     return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)

            # delete a single product
            elif request.method == 'DELETE':
                product.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            # update details of a single product
            elif request.method == 'PUT':
                serializer = ProductSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)
    except KeyError as e:
        print(e)
        return Response({'error': 'bad request'}, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_product_image(request, pid):
    try:
        product = Product.objects.get(pk=pid)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status.HTTP_404_NOT_FOUND)
    img = request.FILES.get('image')
    # post selected image
    if request.method == 'POST':
        # for img in request.FILES.getlist('image'):
        image = ProductImage(image_file=img, product=product)
        image.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product_image(request, pid):
    try:
        image = ProductImage.objects.get(pk=pid)
    except ProductImage.DoesNotExist:
        return Response({'error': 'Image not found'}, status.HTTP_404_NOT_FOUND)

    # delete product image
    if request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
def post_delete_farmer_avatar(request, pid):
    try:
        farmer = Farmer.objects.get(pk=pid)
    except Farmer.DoesNotExist:
        return Response({'error': 'Product not found'}, status.HTTP_404_NOT_FOUND)

    # post selected image
    if request.method == 'POST':
        image = request.FILES.get('image')
        farmer.avatar = image
        farmer.save()
        return Response(status=status.HTTP_201_CREATED)
    # delete product image
    elif request.method == 'DELETE':
        farmer.avatar.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class RequestList(generics.ListAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        requests = Request.objects.all()
        limit = self.request.query_params.get('limit', None)
        offset = self.request.query_params.get('offset', None)
        distance = self.request.query_params.get('distance', None)
        # if limit is not None:
        #     requests = requests.filter(purchaser__username=username)
        # if offset is not None:
        #     requests = requests.filter(purchaser__username=username)
        # if distance is not None:
        #     requests = requests.filter(purchaser__username=username)
        return requests

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({'requests': response.data}, status=status.HTTP_200_OK)
