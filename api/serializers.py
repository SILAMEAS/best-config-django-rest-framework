from rest_framework import serializers
from .models import Product,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= (
            "id",
            "name",
            "price",
            "stock",
            "orders"
        )
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError('Price must be greater than zero')
        return value
    
class ProductInfoSerializer(serializers.Serializer):
    products=ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price= serializers.FloatField()
class OrderItemSerializer(serializers.ModelSerializer):
    product_name= serializers.CharField(source='product.name')
    product_price= serializers.DecimalField(source='product.price',max_digits=10,decimal_places=2)
    class Meta:
        model = OrderItem
        fields= (
            "product_name",
            "product_price",
            "product",
            "quantity",
            "item_subtotal"
        )
    
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')
    def total(seft,obj):
        order_items=obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    class Meta:
        model = Order
        fields= (
            "order_id",
            "create_at",
            "user",
            "status",
            "items"
            "total_price"
        )


