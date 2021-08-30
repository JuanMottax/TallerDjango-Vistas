from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('one/', views.get_measurement, name='oneMeasurement'),
    path('delete/', views.delete_measurement, name='oneDelete')
]