import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://en.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_musicians']

    def parse(self, response):
        print(response)
        xpath = '(//ul)[4]/li/a/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] ='https://en.wikipedia.org/' + s.get()
            print(l)
            yield l
