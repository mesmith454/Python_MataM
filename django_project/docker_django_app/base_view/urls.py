from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('heroes.urls')),
    path('base_view/', views.base_view, name="base_view"),
    path('base_view/<str:name>/', views.greeting, name='greeting'),
    path('admin/', admin.site.urls), 
    path('api/', include('api.urls')),
]