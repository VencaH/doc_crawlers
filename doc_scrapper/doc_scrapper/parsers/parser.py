import abc

class ParserInterface(abc.ABC):

    def __init__(self,response):
        self.response = response

    @abc.abstractmethod
    def get_text(self) -> str:
        pass
    
