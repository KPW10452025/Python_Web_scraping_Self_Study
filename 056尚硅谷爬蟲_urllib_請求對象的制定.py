import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.gamer.com.tw/'

# 尋找網頁 User Agent
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = urllib.request.urlopen(url, headers)

content = response.read().decode('utf-8')

print(content)
# TypeError: can't concat str to bytes
