import pytest
import requests
from config.config_data import accesstoken

@pytest.mark.skip
@pytest.mark.parametrize('x,y',[(1,2),(3,4),(6,5),(8,7)])
def test_xy(x,y):
    assert x > y

test_ddt_data=[
    ({'accesstoken':'','title':'hellords','tab':'ask','content':'cccccccccc'},401,'错误的accessToken'),
    ({'accesstoken':accesstoken,'title':'','tab':'ask','content':'cccccccccc'},400,'标题不能为空'),
    ({'accesstoken':accesstoken,'title':'sfdsdf','tab':'','content':'cccccccccc'},400,'必须选择一个版块'),
    ({'accesstoken':accesstoken,'title':'asdfdsf','tab':'ask','content':''},400,'内容不可为空')
]
@pytest.mark.parametrize('test_data,status_code,expected_error_msg',test_ddt_data)
def test_ddt_topic(test_data,status_code,expected_error_msg):
    creat_url = 'http://49.233.108.117:3000/api/v1/topics'
    r = requests.post(url=creat_url,json=test_data)
    print(r.status_code,r.json())

    assert r.status_code == status_code
    assert r.json()['error_msg'] == expected_error_msg
