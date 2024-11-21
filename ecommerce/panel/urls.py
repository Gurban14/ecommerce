from django.urls import path, include
from panel.views import *

urlpatterns = [
  path('', index_page),
  path('category_table/', category_table),
  path('category_add/', category_form),
  path('category_edit/<int:pk>/', category_edit),
  path('category_delete/<int:pk>/', category_delete),
  path('product_table/', product_table),
  path('product_add/', product_form),
  path('product_edit/<int:pk>/', product_edit),
  path('product_delete/<int:pk>/', product_delete),
  path('order_table/', order_table),
  path('product_details/<int:pk>/', product_details),
  path('order_details/<int:pk>/', order_details),
]