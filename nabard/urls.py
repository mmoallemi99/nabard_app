from django.urls import path

from .views import team_register

app_name = 'nabard'

urlpatterns = [
    path('team_register/', team_register, name='team_register'),
]
