from django.urls import path

from measurement.views import CreateAndGetSensors, GetInfoAndUpdateSensor, AddMeasurements

urlpatterns = [path('sensors/', CreateAndGetSensors.as_view()),
               path('sensors/<pk>/', GetInfoAndUpdateSensor.as_view()),
               path('measurements/', AddMeasurements.as_view())]
