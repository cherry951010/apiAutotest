'''
评论模块
'''

import requests
import pytest
from config.config_data import accesstoken,data,base_url


test_reply_data=[
    ({"accesstoken":accesstoken,"content":'xxxxxxx'},200,{'success':True,'reply_id':'${reply_id}'}),
    ({"accesstoken":accesstoken,"content":'xxxxxxx','reply_id':'${reply_id}'},200,{'success':True,'reply_id':'${reply_id}'})
]

@pytest.mark.run(order = -1)
@pytest.mark.tmp
@pytest.mark.parametrize('reply_data,status_code,except_val',test_reply_data)
def test_reply_topic(reply_data,status_code,except_val):
    topic_id = data['tid']
    url = base_url+f"topic/{topic_id}/replies"
    #如果有replyid字段
    if reply_data.get('reply_id'):
        reply_data['reply_id'] = data['replyid']

    r = requests.post(url=url,json=reply_data)
    print('reply:',r.json())

    if except_val.get('reply_id') == '${reply_id}':
        data['replyid'] = r.json()['reply_id']#将第一次的repylid赋值给变量

    except_val['reply_id'] = r.json()['reply_id']

    assert r.status_code == status_code
    assert r.json() == except_val