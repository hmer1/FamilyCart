from django.urls import path
from . import views

urlpatterns = [
    path('show_list', views.show_list, name='Show The List')
]