from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 通過解析本地文件，來將 bs4 的基礎語法進行講解。
soup = BeautifulSoup(open('075_BeautifulSoup.html', encoding='utf-8'), 'lxml')

# print(soup)

# 第一個符合條件的數據
print(soup.a)
# <a class="a1" href="" id="">尚硅谷</a>

# 第一個符合條件的數據的屬性值
print(soup.a.attrs)
# {'href': '', 'id': '', 'class': ['a1']}

# bs4 的一些函數
# find
# find_all
# select

# find
print(soup.find('a'))
# <a class="a1" href="" id="">尚硅谷</a>
# 返回的是：第一個符合條件的數據

print(soup.find('a',title='a2'))
# <a href="" title="a2">百度</a>
# 根據 title 的值找到對應的標籤對象

print(soup.find('a',class_='a1'))
# <a class="a1" href="" id="">尚硅谷</a>
# 根據 class 的值找到對應的標籤對象
# 注意：查找 html 的 class 值時，必須寫 class_ 因為 python 本身 class 就有定義
