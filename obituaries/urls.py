from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_obituaries, name='obituary_list'),  # Add this line
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('view/', views.view_obituaries, name='view_obituaries'),
]