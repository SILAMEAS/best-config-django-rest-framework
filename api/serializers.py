from rest_framework import serializers
from .models import Product,Order,OrderItem,User
from django.db import transaction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= (
            "id",
            "name",
            "price",
            "stock",
            "orders",
            "description"
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
    order_id=serializers.UUIDField(read_only=True)
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
            "items",
            "total_price"
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields=('product','quantity')
    order_id=serializers.UUIDField(read_only=True)
    items= OrderItemCreateSerializer(many=True,required=False)
    # =======================================================
    #                CREATE ORDER
    # =======================================================
    def create(self, validated_data):
        orderItem_data = validated_data.pop('items')
        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            for orderItem in orderItem_data:
                OrderItem.objects.create(order=order,**orderItem)
        return order
    # =======================================================
    #                UPDATE ORDER
    # =======================================================
    def update(self, instance, validated_data):
        orderItem_data = validated_data.pop('items',None)
        with transaction.atomic():
            instance = super().update(instance,validated_data)
            if orderItem_data is not None:
                # Clear all 
                instance.items.all().delete()
                # Passing 
                for orderItem in orderItem_data:
                    OrderItem.objects.create(order=instance,**orderItem)
        return instance



    class Meta:
        model = Order
        fields= (
            "order_id",
            "user",
            "status",
            "items"
        )
        extra_kwargs={
            'user':{'read_only':True}

        }

