import requests
import pytest
from config.config_data import accesstoken,tid

'''获取主题首页'''
def test_topics():
    home_url = 'http://49.233.108.117:3000/api/v1/topics'
    home_data = {
        'Number':1,
        'tab':'ask',
        'limit':1
    }
    r = requests.get(url=home_url,data=home_data)
    print(r.status_code)
    print(r.json())

'''新建主题'''
@pytest.mark.smoke
def test_creat_topics():
    creat_url = 'http://49.233.108.117:3000/api/v1/topics'
    creat_data = {
        'accesstoken':accesstoken,
        'title':'hellords',
        'tab':'ask',
        'content':'cccccccccc'
    }
    r = requests.post(url=creat_url,json=creat_data)
    tid['tid'] = r.json()['topic_id']
    print(r.status_code)
    print(r.json())

'''获取主题详情'''
def test_detial_topic():
    id = tid['tid']
    detial_url = f'http://49.233.108.117:3000/api/v1/topic/{id}'
    detial_data = {
        'accesstoken':accesstoken
    }
    r = requests.get(url=detial_url,data=detial_data)
    print(r.status_code)
    print(r.json())

'''收藏主题'''
@pytest.mark.smoke
def test_collect_topic():
    id = tid['tid']
    collect_url =f'http://49.233.108.117:3000/api/v1/topic_collect/collect'
    collect_data = {
        'accesstoken':accesstoken,
        'topic_id':id
    }
    r = requests.post(url=collect_url,json=collect_data)
    print(r.status_code)
    print(r.json())
test_creat_topics()
test_collect_topic()

