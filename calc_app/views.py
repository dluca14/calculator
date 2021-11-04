import csv
import pandas as pd

from django.http import HttpResponse

from calc_app.models import RequestModel


def calculate(request):
    # if request.method == 'POST':
    csv_file = request.body.decode()

    col_list = ["S", "V", "T"]
    df = pd.read_csv(csv_file, usecols=col_list)

    # reader = csv.reader(csv_file)
    # for row in reader:
    #     print(row)
        # _, created = RequestModel.objects.get_or_create(
        #     first_name=row[0],
        #     last_name=row[1],
        #     middle_name=row[2],
        # )

    # return HttpResponse(response)


def responses(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
