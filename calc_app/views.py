import csv
import json
from datetime import timedelta
from business_logic.timer import Timer
from business_logic.process_csv_file import get_file_name, get_file_content

from django.http import HttpResponse

from calc_app.models import RequestModel, RowModel, ResponseModel
from calc_app.tasks import process_csv_file


def calculate(request):
    response = process_csv_file.delay(request)

    return response


def responses(request):
    response = []
    for res in ResponseModel.objects.all():
        response.append({
            'request_id': res.request.id,
            'response_id': res.id,
            'calculation_time': res.calculation_time
        })

    return HttpResponse(json.dumps(response), status=200, content_type='json')
