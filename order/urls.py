from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('shopcart', shopcart, name = 'shopcart'),

    path('addtoshopcart/<int:id>', addtoshopcart,name='addtoshopcart'),
    path('deletefromcart/<int:id>', deletefromcart,name='deletefromcart'),




]