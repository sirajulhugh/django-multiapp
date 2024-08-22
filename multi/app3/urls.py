from django.urls import path,include
from .import views

urlpatterns = [
    path('app3',views.b3p1,name="b3p1")
    
]