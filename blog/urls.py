from django.urls import path
from . import views

urlpatterns = [
    path('',views.gonderilistele,name="gonderilistele"), # /blog/
]

