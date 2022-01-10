from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:pk>', views.update, name="update"),
    path('completed/<int:pk>', views.completed, name="completed"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('important/<int:pk>', views.important, name="important"),
    
]