from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('curtir/<int:id>', views.curtir, name='curtir'),
    
]