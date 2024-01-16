from django.urls import path

from measurement.views import sensor_index, SensorList, SensorUpdate, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('', sensor_index),
    path('sensors/', SensorList.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]
