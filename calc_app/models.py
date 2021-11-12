from django.db import models


def calculate_missing_col(s, v, t):
    if s == '':
        s = int(v) * int(t)
    elif v == '':
        v = int(s) / int(t)
    else:
        t = int(s) / int(v)

    return s, v, t


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

