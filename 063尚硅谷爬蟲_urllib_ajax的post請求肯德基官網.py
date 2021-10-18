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

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

if __name__ == "__main__":
    start_page = int(input("請輸入起始頁碼："))
    end_page = int(input("請輸入結束頁碼："))

    for page in range(start_page, end_page + 1):
        print(page)
        