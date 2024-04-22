from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('read_ticket/', views.read_ticket, name='read_ticket'),
    path('delete_ticket/', views.delete_ticket, name='delete_ticket'),
    path('update_ticket/', views.update_ticket, name='update_ticket'),

    path('traitement_ticket', views.traitement_ticket, name='traitement_ticket'),
    path('traitement_category', views.traitement_category, name='traitement_category'),
    
    path('create_category/', views.create_category, name='create_category'),
    path('read_category/', views.read_category, name='read_category'),
    path('delete_category/', views.delete_category, name='delete_category'),
    path('update_category/', views.update_category, name='update_category'),
]
