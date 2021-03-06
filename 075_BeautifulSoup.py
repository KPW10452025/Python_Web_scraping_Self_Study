from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 通過解析本地文件，來將 bs4 的基礎語法進行講解。
soup = BeautifulSoup(open('075_BeautifulSoup.html', encoding='utf-8'), 'lxml')

# print(soup)

# 第一個符合條件的數據
print(soup.a) # <a class="a1" href="" id="">尚硅谷</a>

# 第一個符合條件的數據的屬性值
print(soup.a.attrs) # {'href': '', 'id': '', 'class': ['a1']}

# bs4 的一些函數
# find
# find_all
# select

# find
print(soup.find('a')) # <a class="a1" href="" id="">尚硅谷</a>
# 返回的是：第一個符合條件的數據

print(soup.find('a',title='a2')) # <a href="" title="a2">百度</a>
# 根據 title 的值找到對應的標籤對象

print(soup.find('a',class_='a1')) # <a class="a1" href="" id="">尚硅谷</a>
# 根據 class 的值找到對應的標籤對象
# 注意：查找 html 的 class 值時，必須寫 class_ 因為 python 本身 class 就有定義

# find_all
print(soup.find_all('a')) # [<a class="a1" href="" id="">尚硅谷</a>, <a href="" title="a2">百度</a>]
# 返回的是：一個列表，內容是所有的 a 標籤

print(soup.find_all('a','span')) # []
print(soup.find_all(['a','span'])) # [<a class="a1" href="" id="">尚硅谷</a>, <span>嘿嘿嘿</span>, <a href="" title="a2">百度</a>, <span>哈哈哈</span>]
# 如果想取得多個標籤的數據，那麼在 find_all 的多個參數中添加的是列表的數據

print(soup.find_all('li')) # [<li id="l1">張三</li>, <li id="l2">李四</li>, <li>王五</li>]

print(soup.find_all('li',limit=2)) # [<li id="l1">張三</li>, <li id="l2">李四</li>]
# limit 查找前幾個數據

print(soup.select('a')) # [<a class="a1" href="" id="">尚硅谷</a>, <a href="" title="a2">百度</a>]
# select 方法返回的事一個列表，並且會返回多個數據

print(soup.select('.a1')) # [<a class="a1" href="" id="">尚硅谷</a>]
# 可以通過 . 代表 class 這種操作稱作：類選擇器

print(soup.select('#l1')) # [<li id="l1">張三</li>]
# 可以通過 # 代表 id 這種操作稱作：類選擇器

# 屬性選擇器：通過屬性尋找對應的標籤
# 查找到 li 標籤中有 id 的標籤
print(soup.select('li[id]')) # [<li id="l1">張三</li>, <li id="l2">李四</li>]

# 查找到 li 標籤中 id 為 l2 的標籤
print(soup.select('li[id="l2"]')) # [<li id="l2">李四</li>]

# 層級選擇器
# 後代選擇器
# 長地 div 下面的 li
print(soup.select('div li')) # [<li id="l1">張三</li>, <li id="l2">李四</li>, <li>王五</li>]

# 子代選擇器
# 某標籤的第一層級子標籤
print(soup.select('div > li')) # []
# 因為 div 的第一層子標籤是 ul 所以返回值為空
print(soup.select('div > ul > li')) # [<li id="l1">張三</li>, <li id="l2">李四</li>, <li>王五</li>]
print(soup.select('div>ul>li')) # [<li id="l1">張三</li>, <li id="l2">李四</li>, <li>王五</li>]
# 注意：有些編程語言中，不加空格會報錯，但在 bs4 中不會報錯

# 找到所有 a 與 li 標籤的
print(soup.select('a,li')) # [<li id="l1">張三</li>, <li id="l2">李四</li>, <li>王五</li>, <a class="a1" href="" id="">尚硅谷</a>, <a href="" title="a2">百度</a>]

# 節點訊息，獲取節點內容
obj = soup.select('#d1')[0]
print(obj.string) # None
print(obj.get_text()) # 哈哈哈
# 如果標籤對象中，只有內容，那麼 string 與 get_text() 都可以獲得數據內容
# 如果標籤對象中，除了內容還有標籤，那麼 string 獲取不到數據內容，而 get_text() 可以獲取數據內容
# 所以一般情況下推薦使用 get_text()

# 節點的屬性
obj = soup.select('#p1')
# print(obj.name) # AttributeError: ResultSet object has no attribute 'name'.
# select 返回 list 而 list 沒有 name 屬性

obj = soup.select('#p1')[0]

# name：編嵌的名字
print(obj.name) # p

# attrs：將屬性值作為字典返回
print(obj.attrs) # {'id': 'p1', 'class': ['p1']}

# 獲取節點屬性
obj = soup.select('#p1')[0]
# .attrs 返回字典，用 .get 獲取字典的值
print(obj.attrs.get('class')) # ['p1']

print(obj.get('class')) # ['p1']

print(obj['class']) # ['p1']
