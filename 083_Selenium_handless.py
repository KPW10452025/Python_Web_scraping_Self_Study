from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# handless 有一套默認的基本寫法
# =========================== 默認寫法 ===========================

chrome_options = Options() 
chrome_options.add_argument('--headless')  # 啟動Headless 無頭
chrome_options.add_argument('--disable-gpu') # 關閉GPU 避免某些系統或是網頁出錯

executable_path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver' #看你的Webdrive放哪邊就把路徑指過去

driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options) #套用設定

# =========================== 默認寫法 ===========================

url = 'https://google.com/'

driver.get(url) # 用驅動程式開啟 url

print(driver.title) # 打印頁面 html 的 title
# Google

driver.quit() # 把瀏覽器關閉



