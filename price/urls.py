from django.urls import path
from . import views

urlpatterns=[
    path('simulator', views.addticker, name='simulator'),
    path('',views.index, name='index'),
    path('simulator', views.simulator, name='simulator'),
    path('donations', views.donations, name='donations')
]