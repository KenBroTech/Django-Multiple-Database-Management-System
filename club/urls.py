from django.urls import path
from . import views


urlpatterns = [
    path('club/', views.club, name='club')
]
