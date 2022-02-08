from django.urls import path
from . import views
#importar da propria pasta . views


urlpatterns = [
    path('', views.index)
]