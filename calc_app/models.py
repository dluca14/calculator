from django.db import models


def calculate_missing_col(s, v, t):
    if s is None:
        s = v * t
    elif v is None:
        v = s / t
    else:
        t = s / v

    return s, v, t


class RequestModel(models.Model):
    file_name = models.CharField(max_length=100)


class RowModel(models.Model):
    request_id = models.ForeignKey(RequestModel, on_delete=models.CASCADE, related_name='rows')

    s = models.CharField(max_length=50)
    v = models.CharField(max_length=50)
    t = models.CharField(max_length=50)


class ResponseModel(models.Model):
    request_id = models.ForeignKey(RequestModel, on_delete=models.CASCADE, related_name='response')
    # artist = models.OneToOneField(RequestModel, on_delete=models.CASCADE, primary_key=True)
    calculation_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
