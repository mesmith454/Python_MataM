from django.urls import path
from . import views

urlpatterns = [
    path('heroes/', views.heroes, name="heroes"),
    path('heroes/details/<int:id>', views.details, name='details')
]