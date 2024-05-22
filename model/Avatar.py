from abc import ABC,abstractmethod
import json

class Avatar(ABC):

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def collisio(self,other):
        pass

    @abstractmethod
    def pintar(self,tauler):
        pass

    def __str__(self):
        return json.dumps({'x':self.x,'y':self.y,'width':self.width,'height':self.height})
