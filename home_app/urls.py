from django.urls import path
from home_app import views

urlpatterns = [
    path('',views.vista_inicio,name='vista_inicio')
]
