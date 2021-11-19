import csv
from datetime import timedelta

from business_logic.process_csv_file import get_file_name, get_file_content
from business_logic.timer import Timer
from celery.utils.log import get_task_logger
from django.http import HttpResponse

from celery import shared_task

from calc_app.models import RequestModel, RowModel, ResponseModel

logger = get_task_logger(__name__)


@shared_task
def process_csv_file(request):
    logger.info("Process .csv file request")

    with Timer('calculate_view') as timer:
        decoded_body = request.body.decode()

        file_name = get_file_name(decoded_body)
        req = RequestModel.objects.create(file_name=file_name)

        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="output.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(['S', 'V', 'T'])
        file_content = get_file_content(decoded_body)
        for row in file_content:
            writer.writerow(row.values())
            RowModel.objects.create(s=row['s'], v=row['v'], t=row['t'], request=req)

    ResponseModel.objects.create(
        calculation_time=str(timedelta(seconds=timer.elapsed)),
        calculation_function='s = v * t', request=req)

    logger.info("End process for {} file".format(file_name))

    return response
