from django.urls import path

from .views import *


urlpatterns = [
    path('', indexP, name='indexP'),
    path('addcomment/<int:id>', addcomment, name='addcomment'),

]
