from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .doc_spider import DocSpider
from ..parsers.pa_parser import PaParser
import os


class PaCrawler(DocSpider):
    parser = PaParser
    name = "PA"
    allowed_domains = ["learn.microsoft.com"]
    start_urls = [
        "https://learn.microsoft.com/en-us/power-apps/"
    ]

    rules = [
        Rule(LinkExtractor(allow="en-us/power-apps"), callback = "parse")
    ]
