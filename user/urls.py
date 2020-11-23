from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('login/', login_form, name = 'login_form'),
    path('logout/', logout_func, name = 'logout_func'),
    path('signup/', signup_form, name = 'signup_form'),

    



]