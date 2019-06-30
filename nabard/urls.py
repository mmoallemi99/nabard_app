from django.urls import path

from .views import index, team_register

app_name = 'nabard'

urlpatterns = [
    path('', index, name='index'),
    path('team_register/', team_register, name='team_register'),
]
