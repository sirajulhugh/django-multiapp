from django.urls import path,include
from .import views

urlpatterns = [
    path('b2p1',views.b2p1,name="b2p1"),
    
]