import csv
import json
from datetime import timedelta
from business_logic.timer import Timer
from business_logic.process_csv_file import get_file_name, get_file_content

from django.http import HttpResponse

from calc_app.models import RequestModel, RowModel, ResponseModel
from calc_app.tasks import process_csv_file


def calculate(request):

    with Timer('calculate_view') as timer:
        decoded_body = request.body.decode()

        file_name = get_file_name(decoded_body)
        req = RequestModel.objects.create(file_name=file_name)

        task = process_csv_file.delay(file_name, req.id, decoded_body)

        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="output.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(task.info)

    ResponseModel.objects.create(
        calculation_time=str(timedelta(seconds=timer.elapsed)),
        calculation_function='s = v * t', request=req)

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
