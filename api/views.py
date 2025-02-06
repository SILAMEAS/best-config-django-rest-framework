from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer,ProductInfoSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework import generics,filters
from django.db.models import Max
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.views import APIView
from api.filters import ProductFilter,InStockFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
# ===========================================================
#                   Products List / Create
# ===========================================================
class ProductListCreateAPIView(generics.ListCreateAPIView):
    # .filter(stock__gt=0)  filter product that has stock > 0
    # .exclude(stock__gt=0) filter product that has stock == 0
    queryset = Product.objects.prefetch_related('order_items','orders').order_by('pk')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    search_fields = [
        'name',
        'price',
        'description'
        ]
    filter_backends =[
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        InStockFilterBackend
        ]
    ordering_fields= [
        'name',
        'price',
        'stock'
        ]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5                # if we don't pass this page_size it will take page_size from setting
    pagination_class.page_query_param='pageNum'   # http://localhost:8000/products/?pageNum=5
    pagination_class.page_size_query_param='size' # http://localhost:8000/products/?pageNum=5&size=5
    pagination_class.max_page_size=10             # if size that we pass in url more than max_page_size it only take max_page_size
    # pagination_class = LimitOffsetPagination        # http://localhost:8000/products/?limit=2&offset=8
    def get_permissions(self):
        self.permission_classes =[AllowAny]
        if self.request.method == 'POST':
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()

# ===========================================================
#                   Product Detail
# ===========================================================
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related('order_items','orders').all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        self.permission_classes =[AllowAny]
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()
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
class ProductInfoAPIView(APIView):
    def get(self,request):
        products = Product.objects.prefetch_related("order_items").all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)

