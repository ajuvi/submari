from model.Avatar import Avatar
import json
import math
import pygame

class Submari(Avatar):

    def __init__(self,nom,x,y,width,heigth,path_imatge,velocitat=5):
        super().__init__(x,y,width,heigth)
        self.nom=nom
        self.path_imatge = path_imatge
        self._imatge = pygame.image.load(path_imatge)
        self._imatge = pygame.transform.scale(self._imatge, (width, heigth))
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
        tauler.blit(self._imatge, (self.x,self.y)) 

    def __str__(self):
        return json.dumps({'nom':self.nom,'x':self.x,'y':self.y,'width':self.width,'height':self.height})