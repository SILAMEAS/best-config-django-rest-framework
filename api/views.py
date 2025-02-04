from django.db.models import Max
from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer,ProductInfoSerializer
from api.models import Product,OrderItem,Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404,get_list_or_404

@api_view(['GET'])
def product_list(request):
    products= Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['GET','PUT',"DELETE"])
def product_detail(request,pk):
    product= get_object_or_404(Product,pk=pk)
    if(request.method == 'GET'):
        serializer= ProductSerializer(product)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        serializer= ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET'])
def order_list(request):
    orders= Order.objects.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['GET','PUT',"DELETE"])
def order_detail(request,pk):
    order= get_object_or_404(Order,pk=pk)
    if(request.method == 'GET'):
        serializer= OrderSerializer(order)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        serializer= OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)