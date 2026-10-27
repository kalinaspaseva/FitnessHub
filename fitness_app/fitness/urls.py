from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_trainer, name='edit_trainer'),
    path('book-session/', views.add_session, name='add_session'),
    path('client/add/', views.add_client, name='add_client'),
    path('trainer/<int:pk>/', views.trainer_detail, name='trainer_detail'),
    path('session/<int:pk>/cancel/', views.cancel_session, name='cancel_session'),
]