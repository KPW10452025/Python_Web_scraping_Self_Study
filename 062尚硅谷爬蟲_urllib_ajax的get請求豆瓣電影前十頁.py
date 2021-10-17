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
