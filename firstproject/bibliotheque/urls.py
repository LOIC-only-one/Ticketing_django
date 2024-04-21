from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement', views.traitement),
    path('all/', views.all),
    path('affiche/<int:id>', views.read),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
]