import scrapy


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['https://www.dydytt.net/html/gndy/dyzz/index.html']
    start_urls = ['https://www.dydytt.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # 要第一頁的名字
        # 要第二頁的圖片

        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            print(name, href)
            # 2021年惊悚动作《神偷军团》BD中英双字 /html/gndy/dyzz/20211031/61990.html
            # 2021年剧情《峰爆/无限救援》HD国语中字 /html/gndy/dyzz/20211030/61988.html
            # 2021年剧情惊悚《兰斯基》BD中英双字 /html/gndy/dyzz/20211030/61987.html
            # 2021年剧情爱情《我的青春有个你》HD国语中字 /html/gndy/dyzz/20211026/61982.html
            # 2021年喜剧《五个扑水的少年》HD国语中字 /html/gndy/dyzz/20211026/61981.html
            # 2021年剧情《女人街，再见了》BD国粤双语中字 /html/gndy/dyzz/20211023/61972.html
            # 2021年惊悚《钛/女泰坦/钛妙了》HD中英双字 /html/gndy/dyzz/20211022/61969.html
            # 2021年剧情《把我关起来》BD日语中字 /html/gndy/dyzz/20211021/61966.html
            # 2021年科幻冒险《Dune》HD中英双字 /html/gndy/dyzz/20211020/61963.html
            # 2021年悬疑《信号长期未解决事件搜查组剧场版》BD日语中字 /html/gndy/dyzz/20211018/61960.html
            # 2020年动画《宇宙中最明亮的屋顶》BD日语中字 /html/gndy/dyzz/20211018/61957.html
            # 2021年剧情动作《老亨利》BD中英双字 /html/gndy/dyzz/20211018/61956.html
            # 2021年剧情惊悚《摩加迪沙/绝路狂逃》BD韩语中字 /html/gndy/dyzz/20211017/61953.html
            # 2021年剧情《妈妈的神奇小子》HD国粤双语中字 /html/gndy/dyzz/20211013/61945.html
            # 2021年高分纪录片《九零后》HD国语中字 /html/gndy/dyzz/20211013/61944.html
            # 2020年动画《宝可梦：皮卡丘和可可的冒险》BD国日双语中字 /html/gndy/dyzz/20211011/61940.html
            # 2019年动画《宝可梦：超梦的逆袭进化》BD国日双语中字 /html/gndy/dyzz/20211011/61939.html
            # 2020年科幻《莫斯科陷落2/末日异战》BD国俄双语中字 /html/gndy/dyzz/20211010/61932.html
            # 2011年纪录片《冰血长津湖》HD国语中字 /html/gndy/dyzz/20211010/61931.html
            # 2020年喜剧《回归之路》BD中英双字 /html/gndy/dyzz/20211010/61930.html
            # 2021年恐怖奇幻《绿衣骑士》BD中英双字 /html/gndy/dyzz/20211008/61928.html
            # 2021年动作悬疑《一级指控》HD国粤双语中字 /html/gndy/dyzz/20211008/61927.html
            # 2021年惊悚恐怖《夜间小屋/鬼屋》BD中英双字 /html/gndy/dyzz/20211007/61926.html
            # 2021年惊悚恐怖《逃脱的女孩》BD中英双字 /html/gndy/dyzz/20211007/61925.html
            # 2021年喜剧《日常幻想指南》HD国语中字 /html/gndy/dyzz/20211007/61924.html

        pass
