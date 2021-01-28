from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:pk>', views.company_order, name="order")
    
]
