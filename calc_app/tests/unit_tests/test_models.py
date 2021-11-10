from django.test import TestCase

from calc_app.models import RequestModel, RowModel, ResponseModel


class TestRequestModel(TestCase):
    def setUp(self):
        RequestModel.objects.create(file_name="sample1.csv")

    def test_request_file_name(self):
        r = RequestModel.objects.get(file_name="sample1.csv")

        self.assertTrue(r.file_name, 'sample1.csv')


class TestRowModel(TestCase):
    def setUp(self):
        r = RequestModel.objects.create(file_name="sample1.csv")
        RowModel.objects.create(s='6', v='2', t='3', request=r)
        RowModel.objects.create(s='2', v='1', t='2', request=r)

    def test_calculation(self):
        r = RequestModel.objects.get(file_name="sample1.csv")
        for row in r.rows.all():
            self.assertTrue(row.s, row.v * row.t)


class TestResponseModel(TestCase):
    def setUp(self):
        r = RequestModel.objects.create(file_name="sample1.csv")
        ResponseModel.objects.create(calculation_time="00:00:00.4", calculation_function='s = v * t', request=r)

    def test_function(self):
        r = RequestModel.objects.get(file_name="sample1.csv")
        res = ResponseModel.objects.get(request=r)

        self.assertTrue(res.calculation_function, 's = v * t')
