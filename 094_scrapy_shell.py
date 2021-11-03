# 直接在 terminal 輸入 scrapy shell [url] 即可進入 scrapy shell 模式
# 舉例：scrapy shell wwww.google.com
# 舉例：scrapy shell wwww.baidu.com

# >>> response

# >>> response.status

# >>> response.url

# >>> response.body

# >>> response.text

# >>> a = response.xpath('//input[@id="su"]/@value')
# >>> a
# [<Selector xpath='//input[@id="su"]/@value' data='百度一下'>]

# >>> a.extract_first()
# '百度一下'

# >>> response.css('#su::attr("value")')
# [<Selector xpath="descendant-or-self::*[@id = 'su']/@value" data='百度一下'>]

# >>> a = response.css('#su::attr("value")')
# >>> a.extract_first()
# '百度一下'

