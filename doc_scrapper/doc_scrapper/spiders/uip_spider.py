from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .doc_spider import DocSpider
from ..parsers.uip_parser import UipParser


class UipCrawler(DocSpider):
    parser = UipParser
    name = "UIPath"
    allowed_domains = ["docs.uipath.com"]
    start_urls = [
        "https://docs.uipath.com/activities/other/latest/ui-automation/release-notes-uipath-uiautomation-activities-v24-10"
    ]

    rules = [
        Rule(LinkExtractor(allow="https://docs.uipath.com/activities/other/latest/ui-automation/release-notes-uipath-uiautomation-activities-v24-10"), callback = "parse")
    ]

