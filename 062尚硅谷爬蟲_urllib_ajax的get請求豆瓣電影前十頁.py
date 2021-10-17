import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 觀察 Request URL
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

# 可發現：
# page   1   2   3   4
# start  0   20  40  60

# start = (page - 1)*20

# 下載豆瓣電影前十頁數據

# 基本三步驟：
# 一、請求物件訂製。
# 二、獲取響應數據。
# 三、數據下載到本地。

# 思考邏輯：
# 因為每一頁的 url 都不一樣，所以步驟一要做些改變
# 而每一頁都要經歷步驟二和步驟三

# 設計一個 func 能為每一頁都有自己的請求物件訂製。
# headers 都一樣，所以難點在於 url 的設計。
# 經過上面的觀察發現，url 的差異只有 start 不同。
def create_request():
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': '20',
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers ={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    request = urllib.request.Request(url = url, headers = headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')


# 程式的入口
if __name__ == '__main__':
    start_page = int(input('請輸入起始的頁碼'))
    end_page = int(input('請輸入結束的頁碼'))

    for page in range(start_page, end_page+1):
        # 請求物件訂製
        request = create_request(page)
        # 獲取響應數據
        get_content(request)
