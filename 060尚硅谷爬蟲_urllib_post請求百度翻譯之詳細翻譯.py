import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

# 探討：headers 中，哪個數據最為重要？
# 經由 try and error 註記掉多個數據後發現，只要存在 Cookie 就能破譯出結果

headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '135',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=F461201021999CE52633FDD27744BD23:FG=1; __yjs_duid=1_36b47b97773b6ec30253f93731f41b131631920872152; BAIDUID_BFESS=48738E72741308E4F03E235207029E55:FG=1; BIDUPSID=F461201021999CE52633FDD27744BD23; PSTM=1634356461; H_PS_PSSID=34067_31660_34741_34600_34584_34505_34831_26350_34423_34691; delPer=0; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1634433390,1634433434,1634434046; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1634434046; __yjs_st=2_OTY2NzI2YjI1ZTlkYWM0YTYxZjc1ZGJhYTYyMTAzOTFmMjI2Y2RhOTc0ODE1YzQyMDM5YTU1Yzk5MmUwYzM1N2UzNTgyYTYwMmFlN2FjMmI1NTk1NmNmMGE0ZWI1OTIzM2ZkOGQ2Zjc1OTE2ODA1ZGMxNGVmZjQ5Y2ZjNzQ2M2E4ZWE3MzQyYzMwZTgyMTMzNDdhMGViZWEzY2UwYmNiMGMwZTdiNTVmOGI0NGUzMDkwZTRlYTdmNWZlZDkxMjAwNjEyNTFhN2Y0YWRiMDZjNjViMGU3YWJlY2EyNWE1MDU2NDRhNzk5M2EzMTVjYzA3ODliZjk0ZWIzNDkwMDNjZF83XzQzYjVmZjQ2; ab_sr=1.0.1_MjNmNzExNTgxMGMwNzc4YjczZmI3Mzc5OTc3YjcxNjZkMjcxODI1YjA5NWQ1YWVhMTA5OTI4ODdlNWVkZWRmODhkNjkxMmY0MmRiY2E5NjgzZDg5MDA4NWY2Njg0NTU5OWQzM2MwY2U5OTk1NmM2NTA3ZmQ4ZmI2MWM4ODBhNjVjMmJmNmFmOWIzNTUyYTY3MTkzNDhmMzUyZmJhOGFhZA==',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"macOS"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from' : 'en',
    'to' : 'zh',
    'query': 'love',
    'transtype' : 'realtime',
    'simple_means_flag' : '3',
    'sign' : '198772.518981',
    'token' : 'f956b124540d1acf9353d721879c2974',
    'domain' : 'common',
}

# post 請求的參數必須進行編碼，並且要調用 encode 方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 請求物件的訂製 Constructing a request object.
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模擬瀏覽器向伺服器發送請求，並獲得響應 response
response = urllib.request.urlopen(request)

# 獲得響應 response 的內容 content
content = response.read().decode('utf-8')

import json

obj = json.loads(content)
print(obj)
# {'trans_result': {'data': [{'dst': '爱',......
