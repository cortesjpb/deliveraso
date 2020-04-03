from django.urls import path

from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('routeurl/', views.routeurl, name='routeurl'),
]