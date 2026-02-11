from django.urls import path
from .views import index
from .views import contato

urlpatterns = [

    path('', index),
    path('contato', contato),


]