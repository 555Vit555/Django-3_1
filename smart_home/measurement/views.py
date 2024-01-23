# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorNoMeasureSerializer, AddMeasurementSerializer, SensorSerializer


class CreateAndGetSensors(ListCreateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorNoMeasureSerializer


class GetInfoAndUpdateSensor(RetrieveUpdateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class AddMeasurements(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = AddMeasurementSerializer