from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('crud_operation/',crud_operation),
]
