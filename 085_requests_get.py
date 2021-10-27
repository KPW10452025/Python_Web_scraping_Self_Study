# urllib
# 一、一個類型與六個請求
# 二、get 請求
# 三、post 請求
# 四、ajax 的 get 請求
# 五、ajax 的 post 請求
# 六、cookie 登入
# 七、代理

# requests
# 一、一個類型與六個屬性
# 二、get 請求
# 三、post 請求
# 四、代理
# 五、cookie 驗證碼

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

data = {
    'wd' : '北京'
}

# url 請求資源路徑
# params 參數
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)

content = response.text

print(content)

# 參數使用 params 傳遞
# 參數無需 urlencode 編碼
# 不需要請求物件訂製
