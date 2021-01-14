'''pytest fixture 使用'''
import requests
import  pytest
from config.config_data import accesstoken, data, base_url

@pytest.fixture()
def test_creat_topics():
    creat_url = 'http://49.233.108.117:3000/api/v1/topics'
    creat_data = {
        'accesstoken':accesstoken,
        'title':'hellords',
        'tab':'ask',
        'content':'cccccccccc'
    }
    r = requests.post(url=creat_url,json=creat_data)
    data['tid'] = r.json()['topic_id']
    assert r.status_code == 200
    assert r.json()['success'] == True
    print(r.status_code)
    print(r.json())
    return r.json()['topic_id']

def test_update_topic(test_creat_topics):
    url = base_url+'topics/update'
    update_data = {
        'accesstoken':accesstoken,
        'topic_id':test_creat_topics,
        'title':'ssssssss',
        'tab':'ask',
        'content':'sdfsddfasdf'
    }
    r = requests.post(url=url,json=update_data)
    assert r.status_code == 200