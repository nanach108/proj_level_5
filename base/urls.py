from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('allmyproducts',views.allMyProducts),
    path('mycomputers',views.myComputers),
    path('myphones',views.myPhones),

    path('token/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),


]
