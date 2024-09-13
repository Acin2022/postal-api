from django.urls import path

from .views import CityPostalView

urlpatterns = [
    path('cities/', CityPostalView.as_view(), name='city'),
]