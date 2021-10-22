from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# xpath 解析
# (1) 本地文件
# (2) 服務器響應的數據 response.read().decode('utf-8')
