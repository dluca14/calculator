from __future__ import absolute_import

from io import StringIO
from datetime import timedelta

import csv
from business_logic.process_csv_file import get_file_name, get_file_content
from business_logic.timer import Timer
from celery import shared_task
from celery.utils.log import get_task_logger
from django.http import HttpResponse

from calc_app.models import RequestModel, RowModel, ResponseModel

logger = get_task_logger(__name__)


@shared_task
def process_csv_file(file_name, req_id, decoded_body):
    logger.info("Process .csv file request")

    req = RequestModel.objects.get(id=req_id)

    file_content = get_file_content(decoded_body)
    rows = [['S', 'V', 'T']]
    rows_obj = []
    for row in file_content:
        rows.append([row['s'], row['v'], row['t']])

        rows_obj.append(RowModel(s=row['s'], v=row['v'], t=row['t'], request=req))
    RowModel.objects.bulk_create(rows_obj)

    logger.info("End process for {} file".format(file_name))

    return rows
