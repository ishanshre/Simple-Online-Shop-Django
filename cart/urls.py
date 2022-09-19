from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.cartDetail, name='cart_detail'),
    path('<int:product_id>/add/', views.cartAdd, name='cart_add'),
    path('<int:product_id>/remove/', views.cartRemove, name='cart_remove'),
]