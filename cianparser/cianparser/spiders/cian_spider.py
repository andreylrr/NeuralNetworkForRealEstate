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






# Xpath to links on the page
#'//*[@id="frontend-serp"]/div/div[6]//h3/div/a/@href'

# Xpath to links to other pages
#'//*[@id="frontend-serp"]/div/div[7]//li/a/@href'
#'//*[@id="frontend-serp"]/div/div[7]//li/a/text()'