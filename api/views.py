from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer,ProductInfoSerializer
from api.models import Product,OrderItem,Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import JsonResponse
from django.db.models import Max
from rest_framework.permissions import IsAuthenticated

# ===========================================================
#                   Products List 
# ===========================================================
class ProductListAPIView(generics.ListAPIView):
    # .filter(stock__gt=0)  filter product that has stock > 0
    # .exclude(stock__gt=0) filter product that has stock == 0
    queryset = Product.objects.prefetch_related('order_items','orders').filter(stock__gt=0)
    serializer_class = ProductSerializer

# ===========================================================
#                   Product Detail
# ===========================================================
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('order_items','orders').all()
    serializer_class = ProductSerializer
# ===========================================================
#                   Order List 
# ===========================================================
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer

# ===========================================================
#                   Order Detail
# ===========================================================
class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer

# ===========================================================
#                   Order List By User Login
# ===========================================================
class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
# ===========================================================
#                   Products Info
# ===========================================================
@api_view(['GET'])
def product_info(request):
    products = Product.objects.prefetch_related("order_items").all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)