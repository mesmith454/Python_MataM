from django.urls import path
from . import views

urlpatterns = [
    path('base_view/', views.base_view, name="base_view"),
    path('base_view/<str:name>/', views.greeting, name='greeting'),
]