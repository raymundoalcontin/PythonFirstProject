from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('home/',views.home, name='home'),
    path('add/',views.add, name='add')
]