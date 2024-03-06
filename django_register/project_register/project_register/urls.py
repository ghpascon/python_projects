from django.urls import path
from app_register import views
urlpatterns = [
    #rota, viwe, referencia
    path('', views.home, name= 'home'),
    path('register_p/', views.save_product, name= 'register_product'),
    path('register/', views.register_page, name= 'register_page'),
    path('clear/', views.clear_db, name= 'clear_page'),
]