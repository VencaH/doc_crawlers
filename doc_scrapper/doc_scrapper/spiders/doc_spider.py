from scrapy.spiders import CrawlSpider
from doc_scrapper.parsers.parser import ParserInterface


class DocSpider(CrawlSpider):

    parser: ParserInterface
    
    def parse(self, response) -> dict:
        page = response.url.split("/")[-1]
        folders  = response.url.split("/")[4:]
        content = self.parser(response).get_text()

        # log
        self.log(f"processed page: {page}")
        yield {
            "url": response.url,
            "page": page,
            "route": folders,
            "text": content
        }
