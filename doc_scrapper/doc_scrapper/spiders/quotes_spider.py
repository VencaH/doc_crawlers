from pathlib import Path
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]    
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        quote_text = response.css("div.quote").css("span.text::text").getall();
        author = response.css("div.quote").css("small.author::text").getall();
        quotes = list(zip(quote_text,author))
        for quote in quotes:
            print(quote)
        self.log(f"Saved file {filename}")
