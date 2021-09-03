# author: ZhaoKun
# contact: 1161678627@qq.com
# datetime: 2021-02-26 20:56
# software: PyCharm

import requests
requests.packages.urllib3.disable_warnings()
import time
import schedule

def GetNowTime():
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    date = date[:-3]
    date = date.replace(' ', '日').replace(':', '时') + '分'
    return date

# 登录账户
def login_account(account_data):
    session = requests.session()
    url = 'https://xxcapp.xidian.edu.cn/uc/wap/login/check'
    session.headers = {
        'Host': 'xxcapp.xidian.edu.cn',
        'Origin': 'https://xxcapp.xidian.edu.cn',
        'Referer': 'https://xxcapp.xidian.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fxxcapp.xidian.edu.cn%2Fsite%2Fncov%2Fxidiandailyup',
        'sec-ch-ua': '"GoogleChrome";v="87","Not;ABrand";v="99","Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.141Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = account_data
    response = session.post(url=url, data=data, verify=False)
    if '操作成功' not in response.content.decode():
        # 如果登陆失败，则稍等下再登录
        print(f'时间：{GetNowTime()} 用户{str(data)}登陆失败，正在尝试下一次登录！')
        time.sleep(60)
        session = login_account(account_data)
    else:
        print(f'时间：{GetNowTime()} 用户{str(data)}登陆成功！')
    # session.close()
    # print(response.json())
    return session

# 提交数据
def submit_data(session):
    url = 'https://xxcapp.xidian.edu.cn/ncov/wap/default/save'
    data = {
        'szgjcs': '',
        'szcs': '',
        'szgj': '',
        'zgfxdq': '0',
        'mjry': '0',
        'csmjry': '0',
        'tw': '2',
        'sfcxtz': '0',
        'sfjcbh': '0',
        'sfcxzysx': '0',
        'qksm': '',
        'sfyyjc': '0',
        'jcjgqr': '0',
        'remark': '',
        'address': '陕西省西安市雁塔区电子城街道科技大道南段西安电子科技大学北校区',
        'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"cEa":"jsonp_428024_","position":{"Q":34.23239,"R":108.91516000000001,"lng":108.91516,"lat":34.23239},"message":"GetipLocationsuccess.Getaddresssuccess.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"029","adcode":"610113","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"白沙路","streetNumber":"附8号","country":"中国","province":"陕西省","city":"西安市","district":"雁塔区","township":"电子城街道"},"formattedAddress":"陕西省西安市雁塔区电子城街道科技大道南段西安电子科技大学北校区","roads":[],"crosses":[],"pois":[]}',
        'area': '陕西省西安市雁塔区',
        'province': '陕西省',
        'city': '西安市',
        'sfzx': '1',
        'sfjcwhry': '0',
        'sfjchbry': '0',
        'sfcyglq': '0',
        'gllx': '',
        'glksrq': '',
        'jcbhlx': '',
        'jcbhrq': '',
        'ismoved': '0',
        'bztcyy': '',
        'sftjhb': '0',
        'sftjwh': '0',
        'sfjcjwry': '0',
        'jcjg': ''
    }
    response = session.post(url=url, data=data, verify=False)
    print(response.text)
    session.close()
    return response.text

# 接口
def run(account):
    session = login_account(account)
    submit_data(session)

def test():
    print('程序正常执行中！')

if __name__ == '__main__':
    # run(account=account_data)
    # 设置定时任务
    account_data = {
        'username': '',
        'password': ''
    }
    # 填报时间
    submit_time = "10:17"
    schedule.every().day.at(submit_time).do(run, account_data)
    schedule.every(5).hours.do(test)
    print('程序正常执行中！')
    while True:
        # 运行所有可以运行的任务
        schedule.run_pending()