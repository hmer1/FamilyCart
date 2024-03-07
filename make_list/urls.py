from django.urls import path
from . import views

urlpatterns = [
    path('Make The List/', views.make_list, name='Create The List'),
]