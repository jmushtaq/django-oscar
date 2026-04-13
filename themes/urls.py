from django.urls import path
from . import views

app_name = 'themes'

urlpatterns = [
    path('', views.theme_selector, name='theme-selector'),
]
