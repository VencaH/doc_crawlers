from doc_scrapper.parsers.parser import ParserInterface

class PaParser(ParserInterface):

    def get_text(self) -> str:
        return "".join(
        self.response
        .css("div.mainContainer")
        .xpath(".//main")
        .css("div.content")
        .xpath(".//text()")
        .getall()
        )
    
