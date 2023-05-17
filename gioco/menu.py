import pygame, sys
from pygame.locals import *
from script import Personaggio
from plat import Piattaforma


pygame.init()
WINDOW_SIZE = (1080, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Menu')
display = pygame.Surface((1920,1080)) 

clock = pygame.time.Clock()
fps = 120


class bottone:
    def __init__(self, screen, pos, size) -> None:
        self.screen  = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('git_hub\immagini\pokemon_title-removebg-preview.png')
        
    def draw(self):
        self.screen.blit(self.image, self.rect)

botton_title = bottone(screen, (235, 50), (600, 300))
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pygame.init()
            WINDOW_SIZE = (1920, 1080)
            screen = pygame.display.set_mode((720, 480))
            pygame.display.set_caption('Gioco')

            clock = pygame.time.Clock()
            fps = 120
            piattaforma = Piattaforma(display)
            personaggio = Personaggio(screen, ( 0, 200), (150, 150), piattaforma)
            
            
            while True:
                
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                if personaggio.collide_sx():
                    keys = pygame.key.get_pressed()
                    if keys[K_BACKSPACE]:
                        break
                    elif keys[K_RIGHT]:
                        personaggio.move_right()
                        piattaforma.move_sx()
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

                else:
                    keys = pygame.key.get_pressed()
                    if keys[K_BACKSPACE]:
                        break
                    elif keys[K_RIGHT]:
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
                surf = pygame.transform.scale(display, WINDOW_SIZE)
                screen.blit(display, (0,0))
                personaggio.muovi()
                personaggio.collide_sx()    
                piattaforma.draw()
                personaggio.draw()
                
                
                pygame.display.update()
                clock.tick(fps)

    if keys[K_ESCAPE]:
        break
         
    screen.fill((83, 160, 219))
    
    botton_title.draw()
    pygame.display.update()
    clock.tick(fps)







