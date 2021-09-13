from django.urls import path
from . import views

urlpatterns = [
    path('', views.school, name='school')
]
