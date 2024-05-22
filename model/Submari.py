from model.Avatar import Avatar
import json
import math
import pygame

class Submari(Avatar):

    def __init__(self,nom,x,y,w,h,imatge,velocitat=5):
        super().__init__(x,y,w,h)
        self.nom=nom
        self.imatge=imatge
        self.velocitat=velocitat

    def moure_esquerre(self):
        self.x=self.x-self.velocitat

    def moure_dreta(self):
        self.x=self.x+self.velocitat

    def moure_amunt(self):
        self.y=self.y-self.velocitat

    def moure_avall(self):
        self.y=self.y+self.velocitat

    def pintar(self,tauler):
        tauler.blit(self.imatge, (self.x,self.y)) 

    def __str__(self):
        return json.dumps(self.__dict__)
