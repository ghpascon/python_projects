from django.urls import path
from app_ibov import views
urlpatterns = [
    #rota, viwe, referencia
    path('', views.home, name= 'home'),
    path('online_view/', views.product_register, name= 'product_register'),
    path('email_data/', views.email_get, name= 'email_get'),
]