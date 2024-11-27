from django.urls import path
from . import views

urlpatterns = [
    path('', views.miApp, name='miApp'),
    path('Productos/', views.Productos, name="Productos"),
    path('Bienvenida/', views.Bienvenida, name="Bienvenida"),
]

