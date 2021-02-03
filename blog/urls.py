from django.urls import path
from . import views

urlpatterns = [
    path('',views.gonderilistele,name="gonderilistele"), # /blog/
    path('detay/<int:pk>',views.gonderidetay,name="gonderidetay"),
]

