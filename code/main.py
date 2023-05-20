import pygame, sys
import oggetti
from pygame.locals import *
pygame.init()

WINDOW_SIZE = (720, 1080)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Menu')
screen.fill((0, 200, 0))
schermo = pygame.Surface((720, 1800))
schermo.fill((0, 0, 200))
vel_vert = 10
vel_orizz = 5


clock = pygame.time.Clock()
sfondo = pygame.image.load('image\sfondoy.png')
sfondo = pygame.transform.scale(sfondo, (720, 1080))
fps = 160



    

drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    keys = pygame.key.get_pressed()
    if keys[K_BACKSPACE]:
        break
    elif keys[K_d]:
        drago.move_right()
    else:
        drago.stop_moving_right()
    if keys[K_a]:
        drago.move_left()
    else:
        drago.stop_moving_left() 
    if keys[K_w]:
        drago.move_foward() 
    else:
        drago.stop_moving_foward()
    if keys[K_s]:
        drago.move_back() 
    else:
        drago.stop_moving_back()

    
        
        
    
    screen.fill((0, 200, 0))
    screen.blit(schermo, ((screen.get_width()-schermo.get_width())//2, (screen.get_height()-schermo.get_height())//2 ))
    schermo.fill((0, 0, 200))
    screen.blit(sfondo, (0, 0))
    drago.muovimento()
    drago.disegna()
        
    vel_orizz = 5
    pygame.display.update()
    clock.tick(160)




