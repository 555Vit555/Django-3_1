from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True)