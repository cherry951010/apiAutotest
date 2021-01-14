import time

import requests
import pytest

@pytest.fixture(scope='session',autouse=True)
def session():
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=71b4cd18-0e76-47a5-9b3f-a606d750fd18"
    data = {
        "msgtype":"text",
        "text":{
            "content":"Starting action all TestCases!"
    }
    }
    requests.post(url,json=data)
    yield
    data['text'] = {'content':'all TestCase Complete~!'}
    requests.post(url,json=data)
    time.sleep(4)

