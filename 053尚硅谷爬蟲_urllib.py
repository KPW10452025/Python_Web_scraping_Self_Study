# 使用 urllib 獲取百度首頁的原始碼。
import urllib.request

# MAC 執行爬蟲時需要的必須程序。
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

# 定義一個 url：你要訪問的地址。
url = 'https://www.baidu.com/'

# 模擬瀏覽器像服務器發送請求。
# 運用 urllib.request 發出請求。
# 運用 urlopen(url) 請求開啟一個網址。
# 當一個網站接收到請求時，必定會作出響應，而我們必須要接收響應。
# 這時，運用 reponse 來接收這響應。
response = urllib.request.urlopen(url)

# 獲取響應中的頁面源碼。（因為網站響應後會回傳全部的源碼，這些源碼會夾雜許多我們不要的代碼，必須過濾。）
# 運用 read() 來讀取獲得的響應 response
# 運用 content 來接收讀取 read() 到的響應 response 的內容。
# read() 的方法，返回的是字節形式的二進位數據，這東西是給電腦看的。
# 所以，必須要把二進制的源碼，改成我們能讀得懂的字符串。
# 將二進位轉換成字符串得過程稱作：解碼 decode('編碼的格式')
# 而網站的編碼格式，可以在瀏覽器中檢視網站原始碼中找到。
# charset=utf-8
# charset 字符集，網頁所使用的字符集為 utf-8
content = response.read().decode('utf-8')

# 把內容 content 打印出來
print(content)
