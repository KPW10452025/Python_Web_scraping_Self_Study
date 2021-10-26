from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 把程式進行封裝

def share_dirver():
    chrome_options = Options() 
    chrome_options.add_argument('--headless')  # 啟動Headless 無頭
    chrome_options.add_argument('--disable-gpu') # 關閉GPU 避免某些系統或是網頁出錯
    executable_path = '/Users/kuopowei/Developer/Python/尚硅谷爬蟲/chromedriver' #看你的Webdrive放哪邊就把路徑指過去
    driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options) #套用設定
    return driver

# 使用封裝
driver = share_dirver()

url = 'https://google.com/'

driver.get(url)

print(driver.title) 
# Google

# 頁面截圖 .save_screenshot('圖檔名稱.富檔名稱')
# driver.save_screenshot('google.png')

driver.quit() # 把瀏覽器關閉
