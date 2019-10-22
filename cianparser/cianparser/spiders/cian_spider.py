import scrapy
import urllib.parse as ur

MAXIMUM_PAGE_NUMBER = 100

class CianSpider(scrapy.Spider):
    name = "cianparser"
    start_urls = ['https://spb.cian.ru/kupit-ofis/',]

    def parse(self, response):
        url_split = ur.urlsplit(self.start_urls[0])
        link = response.xpath('//*[@id="frontend-serp"]/div/div[7]//li/a/@href').extract_first()
        url = "https://" + url_split.netloc + link
        print(url)
        for page_number in range(2, MAXIMUM_PAGE_NUMBER):
            l_url = map(lambda x: f"p={page_number}" if "p=" in x else x, url.split("&"))
            s_url_page = "&".join(list(l_url))
            yield scrapy.Request(s_url_page, callback=self.page_parser)

    def page_parser(self, response):
         l_link = response.xpath('//*[@id="frontend-serp"]/div/div[6]//h3//@href')
         for link in l_link:
             yield scrapy.Request(link, callback=self.item_parser)

    def item_parser(self, response):

         pass







# Xpath to links on the page
#'//*[@id="frontend-serp"]/div/div[6]//h3/div/a/@href'
#'//*[@id="frontend-serp"]/div/div[6]//h3//@href'

# Xpath to links to other pages
#'//*[@id="frontend-serp"]/div/div[7]//li/a/@href'
#'//*[@id="frontend-serp"]/div/div[7]//li/a/text()'

# Условия сделки
#'//*[@id="frontend-offer-card"]/main/div[2]/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/text()'