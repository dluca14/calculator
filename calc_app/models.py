from django.db import models


class RequestModel(models.Model):
    s = models.CharField(max_length=50)
    v = models.CharField(max_length=50)
    t = models.CharField(max_length=50)


class ResponseModel(models.Model):
    request_id = models.ForeignKey(RequestModel, on_delete=models.CASCADE, related_name='response')
    # artist = models.OneToOneField(RequestModel, on_delete=models.CASCADE, primary_key=True)
    calculation_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
