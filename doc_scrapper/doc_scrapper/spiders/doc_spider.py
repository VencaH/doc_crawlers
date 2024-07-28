from scrapy.spiders import CrawlSpider
from ..parsers.parser import ParserInterface
from ..items import DocItem

class DocSpider(CrawlSpider):

    parser: ParserInterface
    
    def parse(self, response) -> DocItem:
        page = response.url.split("/")[-1]
        folders  = response.url.split("/")[4:]
        content = self.parser(response).get_text()

        # log
        self.log(f"processed page: {page}")
        yield DocItem(
            url = response.url,
            page = page,
            route = folders,
            text = content
        )
