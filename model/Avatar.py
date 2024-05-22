from abc import ABC,abstractmethod
import json

class Avatar(ABC):

    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y        
        self.w=w
        self.h=h

    @abstractmethod
    def pintar(self,tauler):
        pass

    def __str__(self):
        return json.dumps(self.__dict__)
