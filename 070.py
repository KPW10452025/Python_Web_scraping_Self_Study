from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# xpath 解析
# (1) 本地文件
    # etree.parse()
# (2) 服務器響應的數據 response.read().decode('utf-8')
    # etree.HRML()

# xpath 解析本地文件
tree = etree.parse('070_urllib_xpath.html')

# 語法
# tree01.xpath('//地址')
# 地址開頭一定要加上 //

# '//地址一/地址二‘
# 地址一和地址二是，父類和子類關係

# '//地址三//地址四'
# 地址三和地址四是，爺類和孫類關係

li_list = tree.xpath('//li/text()')
print("The length of li_list =", len(li_list))
# The length of li_list = 11
print(li_list)
# ['台北', '台中', '台南', '台東', '台灣', '美國', '嘉義', '花蓮', '新竹', '桃園', '彰化']

li_list = tree.xpath('//ul')
print("The length of li_list =", len(li_list))
# The length of li_list = 4

li_list = tree.xpath('//ul/ul')
print("The length of li_list =", len(li_list))
# The length of li_list = 1

li_list = tree.xpath('//ul/li')
print("The length of li_list =", len(li_list))
# The length of li_list = 9

li_list = tree.xpath('//ul/ul/li')
print("The length of li_list =", len(li_list))
# The length of li_list = 2

# 尋找所有 li 帶有 id 
li_list = tree.xpath('//li[@id]')
print("The length of li_list =", len(li_list))
# The length of li_list = 6

li_list = tree.xpath('//li[@id]/text()')
print("The length of li_list =", len(li_list))
# The length of li_list = 6
print(li_list)
# ['台北', '台南', '美國', '嘉義', '新竹', '彰化']

li_list = tree.xpath('//li[@id="13"]/text()')
print("The length of li_list =", len(li_list))
# The length of li_list = 1
print(li_list)
# ['美國']

li_list = tree.xpath('//li[@id="88"]/@class')
print(li_list)
# ['t2']

li_list = tree.xpath('//li[contains(@id, "a")]/text()')
print(li_list)
# ['嘉義', '新竹']
