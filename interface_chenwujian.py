# author: ZhaoKun
# contact: 1161678627@qq.com
# datetime: 2021-02-27 23:39
# software: PyCharm

from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()

class Account(BaseModel):
    username: str
    password: str
    xinxiaoqu: int

@app.post('/storage')
def storage(account: Account):
    # 注意account并非json类型，而是一个对象
    username = account.username
    password = account.password
    xinxiaoqu = account.xinxiaoqu
    print(username, password, xinxiaoqu)
    return {'state': 'success'}


if __name__ == '__main__':
    # fast:app 中的fast=运行的文件名,如果修改了记得这里别忘记改
    uvicorn.run("interface_chenwujian:app", host="0.0.0.0", port=8000, reload=True)