import pygame, sys
import oggetti
from pygame.locals import *
from random import randint
pygame.init()
pygame.font.init()
WINDOW_SIZE = (720, 1080)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Menu')
screen.fill((0, 200, 0))
schermo = pygame.Surface((720, 1800))
schermo.fill((0, 0, 200))
vel_vert = 10
vel_orizz = 5

font = pygame.font.SysFont('Arial', 40)
clock = pygame.time.Clock()
sfondo = pygame.image.load('image\sfondoy.png')
sfondo = pygame.transform.scale(sfondo, (720, 1080))
fps = 160
menu_screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo_menu = pygame.image.load('image\sfondoy.png')
sfondo_menu = pygame.transform.scale(sfondo, (720, 1080))



vite_image = pygame.image.load('image\Vite.png')
vite_rect = pygame.Rect((5, 5), (80, 80) )
vite_image = pygame.transform.scale(vite_image, (80, 80))
moneta_image1 = pygame.image.load('image\moneta-removebg-preview (1).png')
moneta_rect1 = pygame.Rect((randint(0, 450), 0), (80, 80) )
moneta_image1 = pygame.transform.scale(moneta_image1,(80, 80))
moneta_image2 = pygame.image.load('image\moneta-removebg-preview (1).png')
moneta_rect2 = pygame.Rect((randint(500, 630), -100), (80, 80) )
moneta_image2 = pygame.transform.scale(moneta_image1,(80, 80))
pokeball_image1 = pygame.image.load('image\pokeball.png')
pokeball_image2 =pygame.image.load('image\pokeball.png')
pokeball_rect1 = pygame.Rect((randint(0, 450), -100), (60, 50) )
pokeball_rect2 = pygame.Rect((randint(500, 660), -100), (60, 50) )
pokeball_image1 = pygame.transform.scale(pokeball_image1,(60, 50))
pokeball_image2 = pygame.transform.scale(pokeball_image2,(60, 50))
vel_pokeball = 1.8
vel_monete = 2.2

def myFunction():
    print('Button Pressed')


start = oggetti.Button(screen, 98, 390, 250, 80, 'Start', myFunction)
skin = oggetti.Button(screen, 358, 390, 250, 80, 'skin', myFunction)
dif_1 = oggetti.Button(screen, 205, 500, 100, 80, '1', myFunction)
dif_2 = oggetti.Button(screen, 310, 500, 100, 80, '2', myFunction)
dif_3 = oggetti.Button(screen, 415, 500, 100, 80, '3', myFunction)


num_collisioni = 0

drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen)

variabile_di_stato ="menu"


while True:
    if variabile_di_stato =="gioco":
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


            moneta_rect1.y+=vel_monete
            if moneta_rect1.y > screen.get_height(): 
                moneta_rect1.y = randint(-800, 0)
                moneta_rect1.x = randint(0, 450)


            moneta_rect2.y += vel_monete
            if moneta_rect2.y > screen.get_height(): 
                moneta_rect2.y = randint(-800, 0)
                moneta_rect2.x = randint(500, 640)

            pokeball_rect1.y += vel_pokeball
            if pokeball_rect1.y > screen.get_height(): 
                pokeball_rect1.y = randint(-800, 0)
                pokeball_rect1.x = randint(0, 450)

            pokeball_rect2.y += vel_pokeball
            if pokeball_rect2.y > screen.get_height(): 
                pokeball_rect2.y = randint(-800, 0)
                pokeball_rect2.x = randint(500, 640)



            if oggetti.collisione_moneta1(moneta_rect1, oggetti.Drago.returna_rect(drago)):
                moneta_rect1.y = randint(-800, 0)
                moneta_rect1.x = randint(0, 450)
        
            elif oggetti.collisione_moneta2(moneta_rect2, oggetti.Drago.returna_rect(drago)):
                moneta_rect2.y = randint(-800, 0)
                moneta_rect2.x = randint(500, 640)
        
            elif oggetti.collisione_pokeball1(pokeball_rect1, oggetti.Drago.returna_rect(drago)):
                pokeball_rect1.y = randint(-800, 0)
                pokeball_rect1.x = randint(0, 450)
                num_collisioni+=1
            elif oggetti.collisione_pokeball2(pokeball_rect2, oggetti.Drago.returna_rect(drago)):
                pokeball_rect2.y = randint(-800, 0)
                pokeball_rect2.x = randint(500, 640)
                num_collisioni+=1
        
            if num_collisioni == 0:
                screen.blit(vite_image, (5, 5))
                screen.blit(vite_image, (85, 5))
                screen.blit(vite_image, (165, 5))
            elif num_collisioni == 1:
                screen.blit(vite_image, (5, 5))
                screen.blit(vite_image, (85, 5))
            elif num_collisioni == 2:
                screen.blit(vite_image, (5, 5))
            else:
                variabile_di_stato = "menu"
                if variabile_di_stato == "menu":
                    break

            screen.blit(moneta_image1, moneta_rect1)
            screen.blit(moneta_image2, moneta_rect2)
            screen.blit(pokeball_image1, pokeball_rect1)
            screen.blit(pokeball_image2, pokeball_rect2)   
            pygame.display.update()
            clock.tick(160)
    elif variabile_di_stato=="menu":
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        
            menu_screen.blit(sfondo_menu, (0,0))
            start.cliccare()
            skin.cliccare()
            dif_1.cliccare()
            dif_2.cliccare()
            dif_3.cliccare()
            variabile_di_stato = start.action()
            if variabile_di_stato ==  "gioco":
                break
            pygame.display.update()
            clock.tick(160)

