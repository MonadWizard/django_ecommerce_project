from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    # path('addcomment/<int:id>', addcomment,name='addcomment'),



]