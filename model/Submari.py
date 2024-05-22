from model.Avatar import Avatar
import json
import math
import pygame

class Submari(Avatar):

    def __init__(self,nom,x,y,width,heigth,path_imatge,velocitat=5):
        super().__init__(x,y,width,heigth)
        self.nom=nom
        self.imatge = pygame.image.load(path_imatge)
        self.imatge = pygame.transform.scale(self.imatge, (width, heigth))
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
