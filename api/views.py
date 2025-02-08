from django.db.models import Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.pagination import (PageNumberPagination)
from api.pagination import CustomPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import InStockFilterBackend, OrderFilter, ProductFilter
from api.models import Order, Product,User
from api.serializers import ( OrderSerializer,
                             ProductInfoSerializer, ProductSerializer,UserDetailSerializer,OrderCreateSerializer,UserSerializer)
from rest_framework.decorators import action


# ===========================================================
#                   Products List / Create
# ===========================================================
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.prefetch_related('order_items','orders').order_by('pk')
    serializer_class = ProductSerializer

    # Search Field
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
    filterset_class = ProductFilter
    # Sort Fields
    ordering_fields= [
        'name',
        'price',
        'stock'
        ]
    pagination_class = CustomPagination
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
# ===========================================================
#                   Order viewsets 
# ===========================================================

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class= OrderSerializer
    filterset_class = OrderFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes=[IsAuthenticated]
    pagination_class = CustomPagination
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_serializer_class(self):
        # POST
        if self.action =='create' or self.action=='update':
            # OrderCreateSerializer
            return OrderCreateSerializer
        return super().get_serializer_class()
    # check if you not admin they just see the order of them if admin can see all of order
    # GET
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

# ===========================================================
#                   User 
# ===========================================================
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    def get_permissions(self):
        self.permission_classes =[AllowAny]
        if self.request.method == 'POST':
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()
class UserUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        self.permission_classes =[IsAuthenticated]
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes=[IsAuthenticated]
    def get_object(self):
        return self.request.user  # Fetches the authenticated user
    