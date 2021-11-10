import csv
import json
import time
from datetime import timedelta

from django.http import HttpResponse

from calc_app.models import RequestModel, RowModel, ResponseModel, calculate_missing_col


def calculate(request):
    start_time = time.time()

    decoded_body = request.body.decode()

    file_name = decoded_body[decoded_body.find('filename=')+10: decoded_body.find('.csv')+4]
    req = RequestModel.objects.create(file_name=file_name)

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="output.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['S', 'V', 'T'])

    cr = csv.reader(decoded_body.splitlines(), delimiter=',')
    my_list = list(cr)
    flag = False
    for row in my_list:
        if flag is True and len(row) == 3:
            s, v, t = calculate_missing_col(row[0], row[1], row[2])
            writer.writerow([str(s), str(v), str(t)])
            RowModel.objects.create(s=s, v=v, t=t, request=req)
        if row == ['S', 'V', 'T']:
            flag = True

    end_time = time.time()
    elapsed = str(timedelta(seconds=end_time - start_time))
    ResponseModel.objects.create(calculation_time=elapsed, calculation_function='s = v * t', request=req)

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
