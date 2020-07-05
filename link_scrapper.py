from string import Template
from typing import DefaultDict
import scrapy
from scrapy.crawler import CrawlerProcess

from consts import PAGE_FULL_URL

class DownloadLinksSpider(scrapy.Spider):
    name = 'download-links-spider'
    # Add custom settings here:
    # custom_settings = { 'DOWNLOD_DELAY': 1 }

    default_last_page_idx = 1
    max_last_page = 1000

    def start_requests(self):
        # found_last_page = self.find_last_page()
        
        page_idx = 0
        while page_idx <= self.default_last_page_idx:
            yield scrapy.http.Request(url=get_page_url(page_idx), callback = self.parse)
            page_idx += 1

    def parse(self, response):
       print(response.body)

    def find_last_page(self) -> int:
        current_last_page = self.default_last_page_idx
        found_last_page = 0
        while found_last_page < self.default_last_page_idx:
            response1 = scrapy.Requests(get_page_url(current_last_page))
            response2 = scrapy.Requests(get_page_url(current_last_page + 1))
            if response1 == response2:
                return current_last_page
            else:
                current_last_page += 1

            if current_last_page > self.max_last_page:
                raise LookupError("Unable to find last page")


def scrap_links():
    process = CrawlerProcess()
    process.crawl(DownloadLinksSpider)
    process.start()


def get_page_url(page_number: int) -> str:
    return Template(PAGE_FULL_URL).substitute(page_number=page_number)
