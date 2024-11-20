from django.urls import path
from . import views

urlpatterns = [
    path('', views.miApp, name='miApp'),
    path('Bienvenida/', views.Bienvenida, name="Bienvenida")
]

