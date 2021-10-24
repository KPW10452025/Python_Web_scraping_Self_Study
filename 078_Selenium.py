# chrome 瀏覽器驅動程式下載地址
# https://chromedriver.storage.googleapis.com/index.html

# chrome 瀏覽器版本查詢辦法
# 點擊瀏覽器右上角符號【 ⋮ 】後點選【 說明 】再點選【 關於 google chrome 】
# 查看版本號

# 安裝 pip install selenium

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 導入 selenium
from selenium import webdriver

url = 'https://www.google.com'

# 創建瀏覽器操作物件

# 輸入 chrome driver 路徑
path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver'
# 啟動 chrome driver
browser = webdriver.Chrome(path)
# 指定開啟網域
browser.get(url)

# 運行後，系統會自動執行 chrome 瀏覽器，並且瀏覽器上面會出現這些字：Chrome 目前受到自動測試軟體控制。
