from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider

class TitlespiderSpider(Spider):
    name = 'blackspider'
    titleList = []
    allowed_domains = ['sxkszx.cn']
    start_urls = ['http://www.sxkszx.cn/news/crgk/index.html',\
                'http://www.sxkszx.cn/news/crgk/index_2.html',\
                'http://www.jseea.cn/enrollment/enrollmentchannel_as_1.html',\
                'http://www.jseea.cn/enrollment/enrollmentchannel_as_2.html',\
                'http://www.bjeea.cn/html/ckcz/tzgg/']

    url_xpath_dic = {'www.sxkszx.cn':"//a[@target='_blank']/text()",\
                    'www.jseea.cn':"//a[@title]/text()",\
                    'www.bjeea.cn':"//div[@id='boss']//li/a/text()"}

    def parse(self, response):
        print '--------------------'
        domain = response.url[7:].split("/")[0]
        if self.url_xpath_dic.has_key(domain):
            execPath = self.url_xpath_dic[domain]
            sel = Selector(response)
            titles = sel.xpath(execPath).extract()
            self.titleList.extend(titles)

        if response.url == self.start_urls[0]:
            with open('titles.txt', 'wb') as titleFile:
                print 'the end with titles:', len(self.titleList)
                for title in self.titleList:
                    print title
                    titleFile.write(title.encode('UTF-8')+"\n")

        print '--------------------'

