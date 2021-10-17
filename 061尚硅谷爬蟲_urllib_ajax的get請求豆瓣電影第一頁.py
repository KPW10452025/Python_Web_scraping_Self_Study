import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# get 請求
# 獲取豆瓣電影的第一頁數據，並保留起來
# https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90

# 尋找目標封包，技巧如下：
# 排除各種 .js .png .css 等檔案。
# 點選 preview 輔助尋找

# 請求物件的訂製 Constructing a request object.
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# 模擬瀏覽器向伺服器發送請求，並獲得響應 response
response = urllib.request.urlopen(request)

# 獲得響應 response 的內容 content
content = response.read().decode('utf-8')

# print(content)
# ue,"id":"1303408","types":["喜剧","动作","爱情"],"regions":["美国"],"title":"福尔摩斯二世",... 成功獲取龐大數據

# 下載數據到本地端
# fp = open('douban.json', mode='w', encoding='utf-8')
# fp.write(content)
# fp.close()
# 成功後會在同資料夾位置，出現一個名為 douban.json 的 json 檔案。

# 小結論
# open 方法默認情況下使用的是 gbk 的編碼，如果我們想要保存漢字，須在 open 方法中指定編碼格式為 utf-8
# 也就是加入 encoding='utf-8'

# 最佳實務寫法
with open('douban.json', mode='w', encoding='utf-8') as fp:
    fp.write(content)
