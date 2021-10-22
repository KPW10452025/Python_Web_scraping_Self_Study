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

# 尋找有幾個 li
li_list = tree.xpath('//li')
print("The length of li_list =", len(li_list))
# The length of li_list = 7

# 尋找有幾個 ul
li_list = tree.xpath('//ul')
print("The length of li_list =", len(li_list))
# The length of li_list = 2
