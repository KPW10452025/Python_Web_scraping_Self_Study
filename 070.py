from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# xpath 解析
# (1) 本地文件
    # etree.parse()
# (2) 服務器響應的數據 response.read().decode('utf-8')
    # etree.HRML()

# tree01 = etree.parse('/Users/kuopowei/Developer/Python/尚硅谷爬蟲/070_urllib_xpath.html')
tree01 = etree.parse('070_urllib_xpath.html')

print(tree01)
