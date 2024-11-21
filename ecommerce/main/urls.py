from django.urls import path, include
from main.views import *
urlpatterns = [
    path('', index_page),
    path('category/<int:pk>/', category),
    path('login/', login_page),
    path('register/', register_page),
    path('logout/', logout_page),
    path('details/<int:pk>/', shop_details),
    path('cart/', shoping_cart),
    path('add_to_cart/<int:pk>/', add_to_cart),
    path('delete_item/<int:pk>/', delete_item),
    path('checkout/', checkout),
    path('save_order/', save_order)
]