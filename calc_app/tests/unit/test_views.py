import json
from datetime import timedelta
import unittest
from unittest.mock import Mock, patch


from calc_app.views import calculate


class MyTestCase(unittest.TestCase):
    def test_calculate(self):
        timer_mock = Mock(elapsed=1)

        request_mock = Mock()
        body = '----------------------------580649799044272887683367\r\nContent-Disposition: form-data; name="file"; filename="sample.csv"\r\nContent-Type: text/csv\r\n\r\nS,V,T\r\n3,5,\r\n2,,3\r\n,4,5\r\n\r\n----------------------------580649799044272887683367--'
        request_mock.body.return_value.decode.return_value = body

        get_file_name_mock = Mock(return_value='sample.csv')

        request_model_mock = Mock()
        request_obj_mock = Mock()
        request_model_mock.objects.return_value.create.return_value = request_obj_mock

        csv_mock = Mock()
        writer_mock = Mock()
        csv_mock.writer.return_value = writer_mock

        content = [{'s': 3.0, 'v': 5.0, 't': 0.6},
                   {'s': 2.0, 'v': 0.6666666666666666, 't': 3.0},
                   {'s': 20.0, 'v': 4.0, 't': 5.0}]
        get_file_content_mock = Mock(return_value=content)

        row_model_mock = Mock()

        response_model_mock = Mock()

        with patch.multiple('calc_app.views',
                            Timer=timer_mock,
                            request=request_mock,
                            get_file_name=get_file_name_mock,
                            RequestModel=request_model_mock,
                            csv=csv_mock,
                            get_file_content=get_file_content_mock,
                            RowModel=row_model_mock,
                            ResponseModel=response_model_mock):
            calculate(request_mock)

            request_mock.body.decode.assert_called_once()
            get_file_name_mock.assert_called_once_with(body)
            request_model_mock.objects.create.assert_called_once_with('sample.csv')

            csv_mock.writer.assert_called_once()
            assert len(writer_mock.writerow.mock_calls) == 4

            assert len(row_model_mock.objects.create.mock_calls) == 3

            response_model_mock.assert_called_once_with(
                calculation_time=str(timedelta(seconds=timer_mock.elapsed)),
                calculation_function='s = v * t', request=request_obj_mock
            )

    def test_responses(self):
        response_mock = Mock(id=1,
                             calculation_time='0.1',
                             request=Mock(id=2))
        response_model_mock = Mock()
        response_model_mock.objects.return_value.all.return_value = [response_mock]
        http_response_mock = Mock()

        with patch.multiple('calc_app.views',
                            ResponseModel=response_model_mock):

            response_model_mock.objects.all.assert_called_once()
            http_response_mock.assert_called_once_with(json.dumps([response_mock]),
                                                       status=200,
                                                       content_type='json')
