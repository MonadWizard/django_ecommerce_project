from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name = 'home'),
    path('category/<int:id>/<slug:slug>', category_products,name='category_products'),
    path('category', category_products,name='category_products_nav'),
    path('search/', search, name='search'),
    path('search_auto/', search_auto, name='search_auto'),
    path('product/<int:id>/<slug:slug>', product_detail,name='product_detail'),



]
