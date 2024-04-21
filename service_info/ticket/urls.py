from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('read_ticket/', views.read_ticket, name='read_ticket'),
    path('delete_ticket/', views.delete_ticket, name='delete_ticket'),
    path('update_ticket/', views.update_ticket, name='update_ticket'),

    path('traitement', views.traitement, name='traitement'),
]
