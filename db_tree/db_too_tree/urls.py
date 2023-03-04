from django.urls import path

from db_too_tree import views

app_name = 'db_too_tree'

urlpatterns = [
    path('<str:title>/', views.index, name='index')
]