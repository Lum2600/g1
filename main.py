import pygame

pygame.init()


erba = pygame.image.load('grass-removebg-preview.png')
drago = pygame.image.load('drago-removebg-preview - Copia inv.png')
sfondo = pygame.image.load('trasferimento__1_-removebg-preview.png')
FPS = 60


SCHERMO = pygame.display.set_mode((720, 480))

def disegna_oggetti():
        SCHERMO.blit(sfondo, (0, 0))
        SCHERMO.blit(drago, (dragox, dragoy))

def aggiorna():
       pygame.display.update()
       pygame.time.Clock().tick(FPS)

def inizializza():
        global dragox, dragoy, drago_velx, drago_vely
        dragox, dragoy = 100, 200
        drago_velx, drago_vely = 5, 5

inizializza()



while True:
    disegna_oggetti()
    aggiorna()