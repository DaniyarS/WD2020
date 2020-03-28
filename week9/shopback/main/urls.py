from django.urls import path

from main.views import product_list, product_id, category, cat_id, cat_prod_id

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_id),
    path('categories/', category),
    path('categories/<int:cat_id>/', cat_id),
    path('categories/<int:cat_id>/products/', cat_prod_id)
]