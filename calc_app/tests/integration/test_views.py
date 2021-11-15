import json

from django.test import TestCase
from django.urls import reverse

from calc_app.models import RequestModel, RowModel, ResponseModel


class CalculateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        r = RequestModel.objects.create(file_name="sample1.csv")

        RowModel.objects.create(s='6', v='2', t='3', request=r)
        RowModel.objects.create(s='2', v='1', t='2', request=r)

        ResponseModel.objects.create(calculation_time="00:00:00.4", calculation_function='s = v * t', request=r)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.put('/calc/calculate')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.put(reverse('calculate'))
        self.assertEqual(response.status_code, 200)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('calculate'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/author_list.html')

    # def test_pagination_is_ten(self):
    #     response = self.client.put(reverse('calculate'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] is True)
    #     self.assertEqual(len(response.context), 2)

    def test_response(self):
        data = '----------------------------406045257029491146236109\r\nContent-Disposition: form-data; name="file"; filename="sample2.csv"\r\nContent-Type: text/csv\r\n\r\nS,V,T\r\n3,5,2,,3\r\n,4,5\r\n\r\n----------------------------406045257029491146236109--\r\n'
        response = self.client.put(reverse('calculate'), data=data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.headers['filename'], 'output.csv')
        self.assertEqual(response.headers['Content-Type'], 'text/csv')
