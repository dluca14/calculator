import csv
import pandas as pd

from django.http import HttpResponse

from calc_app.models import RequestModel, RowModel, ResponseModel, calculate_missing_col


def calculate(request):
    decoded_body = request.body.decode()
    file_name = decoded_body[decoded_body.find('filename=')+10: decoded_body.find('.csv')+4]
    req = RequestModel(file_name=file_name)
    req.save()

    header = ['S', 'V', 'T']

    cr = csv.reader(decoded_body.splitlines(), delimiter=',')
    my_list = list(cr)
    flag = False
    for row in my_list:
        if flag is True and row:
            s, v, t = calculate_missing_col(row[0], row[1], row[2])
            row = RowModel(s=s, v=v, t=t, request_id=req.id)
            row.save()
        if row == header:
            flag = True

    return HttpResponse('all good', status=200)


def responses(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
