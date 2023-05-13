import pygame, sys
from pygame.locals import *
from script import Personaggio
from plat import Piattaforma


pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Menu')
display = pygame.Surface((900, 600)) 

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
            WINDOW_SIZE = (800, 600)
            screen = pygame.display.set_mode(WINDOW_SIZE)
            pygame.display.set_caption('Gioco')

            clock = pygame.time.Clock()
            fps = 120
            piattaforma = Piattaforma(display)
            personaggio = Personaggio(screen, (300, 600), (150, 150))
            # bg = sfondo(screen, ((400,300)), ((800, 600)))
            while True:
    
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    

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
        
                # if personaggio.coll_right() == True:
                #     bg.muove_bg_right()
                # else:
                #     bg.stop_moving_right()
                # if personaggio.coll_right() == True:
                #     bg.muove_bg_left()
                # else:
                #     bg.stop_moving_left()
                # if personaggio.coll_foward() == True:
                #     bg.muove_bg_foward()
                # else:
                #     bg.stop_moving_foward()
                # if personaggio.coll_back() == True:
                #     bg.muove_bg_foward()
                # else:
                #     bg.stop_moving_back()


                    
                screen.fill((69, 173, 75))
                surf = pygame.transform.scale(display, WINDOW_SIZE)
                screen.blit(surf, (0,0))
                # bg.draw()
                personaggio.muovi()
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







#             
            
#                 
#     if keys[K_ESCAPE]:
#         break
#     #chiedi al prof come spawnare i cespulgi a caso
              

#     screen.fill((83, 160, 219))
#     botton_title.draw()
#     pygame.display.update()
#     clock.tick(fps)




