# location/urls.py
from django.urls import path
from .views import ZipCodeView

urlpatterns = [
    path('get_location/', ZipCodeView.as_view(), name='get_location'),
]
