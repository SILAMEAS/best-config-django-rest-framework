import django_filters
from api.models import Product,Order
from rest_framework import filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields= {
            'name': ['iexact','icontains'],
            'price':['exact','lt','gt','range']
        }

class InStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        return queryset.filter(stock__gt=0)
    
class OrderFilter(django_filters.FilterSet):
    create_at= django_filters.DateFilter(field_name='create_at__date')
    class Meta:
        model = Order
        fields ={
            'status':['exact'],
            'create_at':['exact','gt','lt']
        }


    # .filter(stock__gt=0)  filter product that has stock > 0
    # .exclude(stock__gt=0) filter product that has stock == 0