from __future__ import absolute_import
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
def process_csv_file(a, b):
    logger.info("Process .csv file request")

    # logger.info("End process for {} file".format(file_name))

    return a + b
