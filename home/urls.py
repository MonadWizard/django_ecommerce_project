from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name = 'index'),
    path('category/<int:id>/<slug:slug>', category_products,name='category_products'),



]
