from django.urls import path
from .views import portfoliya

urlpatterns = [
    path('', portfoliya, name='portfoliya'),
]