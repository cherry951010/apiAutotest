import pytest
import requests
from  file_tools.csv_handler import read_csv_to_dict
import os

topic_data_file = os.path.join(os.path.dirname(__file__),'../test_data_files/data.csv')
testdata = read_csv_to_dict(topic_data_file)
print(testdata)




@pytest.mark.parametrize('test_data,status_code,expected_error_msg',testdata)
def test_ddt_topic(test_data,status_code,expected_error_msg):
    creat_url = 'http://49.233.108.117:3000/api/v1/topics'
    r = requests.post(url=creat_url,json=test_data)
    print(r.status_code,r.json())

    assert r.status_code == status_code
    assert r.json()['error_msg'] == expected_error_msg