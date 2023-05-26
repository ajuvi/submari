import pygame
from model.Submari import Submari
from dades.Persistencia import Persistencia
import datetime
from threading import Thread
from time import sleep

def main():
    # Inicialitzar Pygame
    pygame.init()
    fpsClock = pygame.time.Clock()

    # Paràmetres del joc
    FPS = 60
    screen_width=800
    screen_height=600

    # Crear la finestra (screen) i la zona per a pintar (tauler)
    screen = pygame.display.set_mode((screen_width, screen_height))
    tauler = pygame.Surface((screen_width, screen_height))

    # Text de la finestra
    pygame.display.set_caption("Submarine Project")

    # Configurar la lectura del teclat
    pygame.key.set_repeat(1, 50)

    # Crear l'objecte del submari
    sub = Submari('ictineu',screen_width/4,screen_height/2,20,30,pygame.image.load('./imatges/submari.png'))

    # Registrar el temps
    temps_inici = datetime.datetime.now()

    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    raise NotImplementedError("Has de moure a l'esquerre el submari") 
                if evento.key == pygame.K_RIGHT:
                    raise NotImplementedError("Has de moure a la dreta el submari") 
                if evento.key == pygame.K_UP:
                    raise NotImplementedError("Has de moure amunt el submari") 
                if evento.key == pygame.K_DOWN:
                    raise NotImplementedError("Has de moure avall el submari") 

        # Pintar el tauler de blau
        tauler.fill((0, 0, 25)) 

        # Pintar el submari
        #raise NotImplementedError("Has de pintar el submari en el tauler utilitzant el mètode pintar") 

        # Registrar posicions del submarí
        if (datetime.datetime.now()-temps_inici).seconds > 1:                       
            temps_inici=datetime.datetime.now()
            # Crea un nou fill d'execució per a insertar a la base de dades
            Thread(target=afegir_mesura, args=[sub.nom,sub.x,sub.y]).start()
 
        # Aplicar el doble buffering        
        screen.blit(tauler, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS)

# Mètode que s'executa a dins d'un thread
def afegir_mesura(nom,x,y):
    try:
        raise NotImplementedError("Has d'inserir les dades a la base de dades") 
    except Exception as e:
        print('Error en inserir a la base de dades. ' + str(e))

if __name__ == "__main__":
    main()
