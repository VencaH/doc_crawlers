from doc_scrapper.parsers.parser import ParserInterface

class UipParser(ParserInterface):

    def get_text(self) -> str :
        lines = [line for line in
            self.response
            .xpath("//body/div[1]")
            .xpath("div[1]")
            .xpath("div[2]")
            .xpath("div[1]")
            .xpath("div[2]")
            .xpath("div[1]")
            .xpath("div[1]")
            .xpath("div[2]")
            .xpath("div[4]")
            .xpath("div[1]")
            .xpath("div[3]")
            .xpath("div[3]")
            .xpath('.//*[ name() = "h1" or name() = "h2" or name() = "h3" or name() = "p" or name() = "a"]')
            .xpath(".//text()")
            .getall()
        ]        
        return "".join(lines)    
