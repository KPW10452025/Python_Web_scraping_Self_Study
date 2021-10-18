# 目標：爬取 可德基北京店鋪分佈原始碼
# http://www.kfc.com.cn/kfccda/storelist/index.aspx

# 第一頁
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# POST
# cname: 北京
# pid: 
# pageIndex: 1
# pageSize: 10

# 第二頁
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# POST
# From data:
# cname: 北京
# pid: 
# pageIndex: 2
# pageSize: 10

# 第三頁
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# POST
# cname: 北京
# pid: 
# pageIndex: 3
# pageSize: 10

# 經觀察可以發現差異在 pageIndex 這個 data

import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def create_request(page):
    # create_request() 的基本三要素：url, data, headers
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10,
    }
    # 和 GET 不一樣的是，POST 的 urllib.parse.urlencode(data) 後面要加個 encode("utf-8")
    data = urllib.parse.urlencode(data).encode("utf-8")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    request = urllib.request.Request(url = base_url, data = data, headers = headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")

if __name__ == "__main__":
    start_page = int(input("請輸入起始頁碼："))
    end_page = int(input("請輸入結束頁碼："))

    for page in range(start_page, end_page + 1):
        print(page)
        # 請求物件訂製
        create_request(page)
        # 獲取響應數據
        content = get_content(request)
