from django.urls import path

from . import views

app_name = 'producer_consumer'

urlpatterns = [
    path('', views.log_in),
    path('logout/', views.log_out),
    path('orders/', views.orders_list, name='orders_list'),
    path('close-order/<int:order_id>', views.delete_order, name='delete_order'),
]
