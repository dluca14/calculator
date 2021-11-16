from unittest.mock import Mock, patch, MagicMock

from calc_app import views


def test_calculate():
    timedelta_mock = Mock(return_value=1)

    timer_obj_mock = Mock(elapsed=1)
    timer_class_mock = MagicMock()
    timer_class_mock.__enter__.return_value = timer_obj_mock

    body = '----------------------------580649799044272887683367\r\nContent-Disposition: form-data; name="file"; filename="sample.csv"\r\nContent-Type: text/csv\r\n\r\nS,V,T\r\n3,5,\r\n2,,3\r\n,4,5\r\n\r\n----------------------------580649799044272887683367--'
    request_mock = Mock()
    request_mock.body.decode.return_value = body

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
    response_model_mock.objects.create.return_value = Mock()

    with patch.multiple('calc_app.views',
                        timedelta=timedelta_mock,
                        Timer=timer_class_mock,
                        get_file_name=get_file_name_mock,
                        RequestModel=request_model_mock,
                        csv=csv_mock,
                        get_file_content=get_file_content_mock,
                        RowModel=row_model_mock,
                        ResponseModel=response_model_mock):
        views.calculate(request_mock)

        request_mock.body.decode.assert_called_once()
        get_file_name_mock.assert_called_once_with(body)
        request_model_mock.objects.create.assert_called_once_with(file_name='sample.csv')

        csv_mock.writer.assert_called_once()
        assert len(writer_mock.writerow.mock_calls) == 4

        assert len(row_model_mock.objects.create.mock_calls) == 3

        timedelta_mock.assert_called_once()
        response_model_mock.objects.create.assert_called_once_with(
            calculation_time=str(1),
            calculation_function='s = v * t', request=request_obj_mock
        )
        # response_model_mock.assert_called_once_with(
        #     calculation_time=str(timedelta(seconds=timer_mock.elapsed)),
        #     calculation_function='s = v * t', request=request_obj_mock
        # )


def test_responses():
    response_mock = Mock(id=1,
                         calculation_time='0.1',
                         request=Mock(id=2))
    response_model_mock = MagicMock()
    response_model_mock.objects.all.return_value = [response_mock]
    http_response_mock = Mock()

    json_mock = Mock()
    dump_mock = Mock()
    json_mock.dumps.return_value = dump_mock

    with patch.multiple('calc_app.views',
                        ResponseModel=response_model_mock,
                        HttpResponse=http_response_mock,
                        json=json_mock):
        views.responses(Mock())

        response_model_mock.objects.all.assert_called_once()
        http_response_mock.assert_called_once_with(dump_mock,
                                                   status=200,
                                                   content_type='json')
