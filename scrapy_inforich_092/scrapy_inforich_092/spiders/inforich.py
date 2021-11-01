import scrapy


class InforichSpider(scrapy.Spider):
    name = 'inforich'
    allowed_domains = ['https://www.inforich-corp.com/']
    start_urls = ['https://www.inforich-corp.com/']

    def parse(self, response):
        # span = response.xpath('//div[@class="col-12"]/span/text()')
        span = response.xpath('//*[@id="about"]/div/div/div[2]/div/div[2]/span/text()')
        print("****************************")
        print(span.extract_first())
        print("****************************")
# ****************************
# Inforich was founded in 2015, based in HsinChu Technology Park, with core technology in areas of Network Security , and cloud-based embedded control software. The product application areas include :
# ****************************
# 爬取成功
