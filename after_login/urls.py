from django.urls import path
from . import views

urlpatterns = [
    path('after_login', views.after_login, name='after_login')
]