from abc import ABC,abstractmethod
import json

class Avatar(ABC):

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y        
        self.width=width
        self.height=height

    @abstractmethod
    def pintar(self,tauler):
        pass

    def __str__(self):
        return json.dumps(self.__dict__)
