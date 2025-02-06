from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('products/',views.ProductListCreateAPIView.as_view()),
    path('products/<int:pk>',views.ProductDetailAPIView.as_view()),
    path('user-detail/',views.UserDetailAPIView.as_view()),
    path('products/info/',views.ProductInfoAPIView.as_view()),
    path('users/',views.UserListCreateAPIView.as_view()),
    path('users/<int:pk>',views.UserUpdateDestroyAPIView.as_view())
]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)

urlpatterns+=router.urls