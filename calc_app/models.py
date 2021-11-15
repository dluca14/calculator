from django.db import models


class RequestModel(models.Model):
    file_name = models.CharField(max_length=100)


class RowModel(models.Model):
    s = models.FloatField(max_length=50)
    v = models.FloatField(max_length=50)
    t = models.FloatField(max_length=50)

    request = models.ForeignKey(RequestModel, on_delete=models.CASCADE, related_name='rows')


class ResponseModel(models.Model):
    calculation_time = models.CharField(max_length=100)
    calculation_function = models.CharField(max_length=100)

    request = models.ForeignKey(RequestModel, on_delete=models.CASCADE, related_name='response')

