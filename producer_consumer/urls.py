from django.urls import path

from . import views

app_name = 'producer_consumer'

urlpatterns = [
    path('', views.information_about_all_users, name='list'),
]