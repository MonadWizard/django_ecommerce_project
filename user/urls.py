from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('login/', login_form, name = 'login_form'),
    path('logout/', logout_func, name = 'logout_func'),
    path('signup/', signup_form, name = 'signup_form'),
    path('update/', user_update, name = 'user_update'),
    path('password/', user_password, name = 'user_password'),
    path('orders/', user_orders, name = 'user_orders'),
    path('orderdetail/<int:id>', user_orderdetail,name='user_orderdetail'),
    path('orders_product/', user_order_product, name = 'user_order_product'),
    path('order_product_detail/<int:id>/<int:oid>', user_order_product_detail, name = 'user_order_product_detail'),





    



]