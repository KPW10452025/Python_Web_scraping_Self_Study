import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    # 當 url 後綴是 html 時，不能加 /
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):

        # print("***************this is for testing***************")
        # ***************this is for testing*************** 爬蟲成功

        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        # print(name_list)
        # Selector 的 list
        # [<Selector xpath='//div[@class="main-title"]/a/text()' data='宝马1系'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马3系'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马5系'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马5系新能源'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X1'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X1新能源'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X2'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马iX3'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X3'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马2系'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马4系'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马5系(进口)'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马6系GT'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马7系'>, <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马8系'>]
        
        # for name in name_list:
            # print(name)
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马1系'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马3系'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马5系'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马5系新能源'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X1'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X1新能源'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X2'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马iX3'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马X3'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马2系'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马4系'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马5系(进口)'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马6系GT'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马7系'>
            # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马8系'>

            # print(name.extract())
            # 宝马1系
            # 宝马3系
            # 宝马5系
            # 宝马5系新能源
            # 宝马X1
            # 宝马X1新能源
            # 宝马X2
            # 宝马iX3
            # 宝马X3
            # 宝马2系
            # 宝马4系
            # 宝马5系(进口)
            # 宝马6系GT
            # 宝马7系
            # 宝马8系
        
        price_list = response.xpath('//span[@class="font-arial"]/text()')
        # for price in price_list:
        #     print(price.extract())
            # 20.58-24.68万
            # 29.39-39.89万
            # 42.39-55.19万
            # 49.99-53.69万
            # 27.98-33.98万
            # 39.98万
            # 28.58-32.38万
            # 39.99-43.99万
            # 39.28-47.98万
            # 26.38-33.98万
            # 36.38-55.88万
            # 42.39-60.39万
            # 58.39-68.39万
            # 82.80-261.20万
            # 96.20-119.80万
        
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)
            # 宝马1系 20.58-24.68万
            # 宝马3系 29.39-39.89万
            # 宝马5系 42.39-55.19万
            # 宝马5系新能源 49.99-53.69万
            # 宝马X1 27.98-33.98万
            # 宝马X1新能源 39.98万
            # 宝马X2 28.58-32.38万
            # 宝马iX3 39.99-43.99万
            # 宝马X3 39.28-47.98万
            # 宝马2系 26.38-33.98万
            # 宝马4系 36.38-55.88万
            # 宝马5系(进口) 42.39-60.39万
            # 宝马6系GT 58.39-68.39万
            # 宝马7系 82.80-261.20万
            # 宝马8系 96.20-119.80万
            