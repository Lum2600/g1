import pygame, sys
from pygame.locals import *
from script import Personaggio
from script import bush
from script import schermo
from random import randint

pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Gioco')

clock = pygame.time.Clock()
fps = 120

personaggio = Personaggio(screen, (300, 600), (150, 150))

while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        personaggio.move_right()
    else:
        personaggio.stop_moving_right()
    if keys[K_LEFT]:
        personaggio.move_left()
    else:
        personaggio.stop_moving_left() 
    if keys[K_UP]:
        personaggio.move_foward() 
    else:
        personaggio.stop_moving_foward()
    if keys[K_DOWN]:
        personaggio.move_back() 
    else:
        personaggio.stop_moving_back()
        
    
    screen.fill((69, 173, 75))
    
    
     
    personaggio.muovi()
    

    
    personaggio.draw()
    personaggio.camera_dx()
    pygame.display.update()
    clock.tick(fps)


    #chiedi al prof come spawnare i cespulgi a caso