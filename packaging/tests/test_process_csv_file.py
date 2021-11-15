from unittest.mock import Mock, patch

from packaging.src.business_logic.process_csv_file import get_file_name, get_file_content


def test_get_file_name():
    body = '----------------------------580649799044272887683367\r\nContent-Disposition: form-data; name="file"; filename="sample.csv"\r\nContent-Type: text/csv\r\n\r\nS,V,T\r\n3,5,\r\n2,,3\r\n,4,5\r\n\r\n----------------------------580649799044272887683367--'
    file_name = get_file_name(body)

    assert file_name == 'sample.csv'


def test_get_file_content():
    csv_mock = Mock()
    csv_mock.reader.return_value = [[],[],[],[],[],['3', '5', ''],['2', '', '3'],['', '4', '5'],[],[]]

    with patch.multiple('packaging.src.business_logic.process_csv_file',
                        csv=csv_mock):
        content = get_file_content(Mock())

        assert content == [{'s': 3.0, 'v': 5.0, 't': 0.6},
                           {'s': 2.0, 'v': 0.6666666666666666, 't': 3.0},
                           {'s': 20.0, 'v': 4.0, 't': 5.0}]
