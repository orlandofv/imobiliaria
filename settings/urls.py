from django.urls import path

from .views import settings_create_view

app_name = 'settings'

urlpatterns = [
    path('settings/', settings_create_view, name='settings_view')
    
]