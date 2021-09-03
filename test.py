# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-02-18 16:47
# software: PyCharm

import requests
import json

# post的参数必须要json.dumps一下才能传入
data = json.dumps({'username': 123, 'password': 23})
res = requests.post(url='http://127.0.0.1:8000/storage', data=data)
print(res.text)