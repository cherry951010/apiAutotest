import requests
import pytest
from config.config_data import accesstoken,data

'''收藏主题'''
@pytest.mark.smoke
def test_collect_topic():
    id = data['tid']
    collect_url =f'http://49.233.108.117:3000/api/v1/topic_collect/collect'
    collect_data = {
        'accesstoken':accesstoken,
        'topic_id':id
    }
    r = requests.post(url=collect_url,json=collect_data)
    assert r.json()['success'] == True
    print(r.status_code)
    print(r.json())