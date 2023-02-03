from django.urls import path
from .views import *

urlpatterns = [path('ap/', Add_Invent_API.as_view())]