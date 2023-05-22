import pygame, sys
import oggetti
from pygame.locals import *
from random import randint
pygame.init()
pygame.font.init()
pygame.mixer.init()


#schermo del gioco
WINDOW_SIZE = (720, 1080)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('gioco')
screen.fill((0, 200, 0))
schermo = pygame.Surface((720, 1800))
schermo.fill((0, 0, 200))
sfondo = pygame.image.load('image\sfondoy.png')
sfondo = pygame.transform.scale(sfondo, (720, 1080))
#schermo del menu
menu_screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo_menu = pygame.image.load('image/sfondoy.png')
sfondo_menu = pygame.transform.scale(sfondo, (720, 1080))
logo_image= pygame.image.load('image/lgo-removebg-preview.png')

#schermo del gameover
game_over_screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo_game_over = pygame.image.load("image\sfondo_over.jpg")
sfondo_game_over = pygame.transform.scale(sfondo_game_over, (720, 1080))

#musica
ost = pygame.mixer.music.load("image\X2Download.app - 1 Hour of Relaxing Pokemon HeartGold_SoulSilver Music Compilation (128 kbps).mp3")
pygame.mixer_music.set_volume(1.0)
score_100 = pygame.mixer.Sound('image\Mario Jump Sound Effect.mp3')

#costanti di gioco
vel_vert = 10
vel_orizz = 5
font = pygame.font.SysFont('Arial', 40)
score = 0
clock = pygame.time.Clock()
fps = 160
vel_pokeball = 1.8
vel_monete = 2.2
num_collisioni = 0
variabile_di_stato ="menu"
TIMERSHOT = pygame.event.custom_type()
pygame.time.set_timer(TIMERSHOT, 500)
incremento_al_sec= 1

#immagini png
vite_image = pygame.image.load('image/Vite.png')
vite_rect = pygame.Rect((5, 5), (80, 80) )
vite_image = pygame.transform.scale(vite_image, (80, 80))
moneta_image1 = pygame.image.load('image/moneta-removebg-preview (1).png')
moneta_rect1 = pygame.Rect((randint(0, 450), 0), (80, 80) )
moneta_image1 = pygame.transform.scale(moneta_image1,(80, 80))
moneta_image2 = pygame.image.load('image/moneta-removebg-preview (1).png')
moneta_rect2 = pygame.Rect((randint(500, 630), -100), (80, 80) )
moneta_image2 = pygame.transform.scale(moneta_image1,(80, 80))
pokeball_image1 = pygame.image.load('image/pokeball.png')
pokeball_image2 =pygame.image.load('image/pokeball.png')
pokeball_rect1 = pygame.Rect((randint(0, 450), -100), (60, 50) )
pokeball_rect2 = pygame.Rect((randint(500, 660), -100), (60, 50) )
pokeball_image1 = pygame.transform.scale(pokeball_image1,(60, 50))
pokeball_image2 = pygame.transform.scale(pokeball_image2,(60, 50))




def myFunction():
    print('Button Pressed')

#bottoni
start = oggetti.Button((250, 225, 2),screen, 98, 390, 250, 80, 'Start', myFunction)
skin = oggetti.Button((250, 225, 2),screen, 358, 390, 250, 80, 'skin', myFunction)
dif_1 = oggetti.Button((250, 225, 2),screen, 205, 500, 100, 80, '1', myFunction)
dif_2 = oggetti.Button((250, 225, 2),screen, 310, 500, 100, 80, '2', myFunction)
dif_3 = oggetti.Button((250, 225, 2),screen, 415, 500, 100, 80, '3', myFunction)
game_over = oggetti.Button((27, 42, 207),screen, 180, 550, 400, 100, 'Riprova', myFunction)



#giocatore
drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen)




while True:
    pygame.mixer.music.play(-1)
    if variabile_di_stato=="menu":
        
        variabile_di_stato = "menu"
        run = True
        while run:
            
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[K_BACKSPACE]:
                    break

            menu_screen.blit(sfondo_menu, (0,0))
            screen.blit(logo_image, (180,100))
            start.cliccare()
            skin.cliccare()
            dif_1.cliccare()
            dif_2.cliccare()
            dif_3.cliccare()
            if start.action():
                variabile_di_stato = "gioco"
            if variabile_di_stato ==  "gioco":
                run = False
                break
            
            print(variabile_di_stato)
            pygame.display.update()
            clock.tick(160)

    
    if variabile_di_stato =="gioco":
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == TIMERSHOT:
                    score+=incremento_al_sec
                    print("timer +")
                
                    
                
                
                     
            keys = pygame.key.get_pressed()

            if keys[K_m]:
                drago.pausa()
                vel_monete = 0
                vel_pokeball = 0
                incremento_al_sec = 0
                
            if keys[K_n]: 
                vel_pokeball = 1.8
                vel_monete = 2.2
                drago.btg()
                incremento_al_sec = 1
                
            if keys[K_BACKSPACE]:
                    break
            if keys[K_d]:
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
            
            if (score+1000)%1000== 0 and score!=0:
                pygame.mixer.Sound.set_volume(score_100, 0.1)
                pygame.mixer.Sound.play(score_100)
                
                   
            
                
                
            # else:
            #     pygame.mixer_music.load("image\X2Download.app - 1 Hour of Relaxing Pokemon HeartGold_SoulSilver Music Compilation (128 kbps).mp3")
            #     pygame.mixer_music.set_volume(0.5)
            #     pygame.mixer_music.play()

                

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
                score +=10
        
            elif oggetti.collisione_moneta2(moneta_rect2, oggetti.Drago.returna_rect(drago)):
                moneta_rect2.y = randint(-800, 0)
                moneta_rect2.x = randint(500, 640)
                score +=10
        
        
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
                variabile_di_stato = "game_over"
                
                if variabile_di_stato !="gioco":
                    moneta_rect1.y = randint(-800, 0)
                    moneta_rect1.x = randint(0, 450)
                    score +=10
                    moneta_rect2.y = randint(-800, 0)
                    moneta_rect2.x = randint(500, 640)
                    score +=10
                    pokeball_rect1.y = randint(-800, 0)
                    pokeball_rect1.x = randint(0, 450)
                    num_collisioni+=1
                    pokeball_rect2.y = randint(-800, 0)
                    pokeball_rect2.x = randint(500, 640)
                    num_collisioni+=1
                    drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen)
                    num_collisioni = 0
                    score = 0
                    run = False
                    break
                    

            screen.blit(moneta_image1, moneta_rect1)
            screen.blit(moneta_image2, moneta_rect2)
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(score_text, (500, 10))
            screen.blit(pokeball_image1, pokeball_rect1)
            screen.blit(pokeball_image2, pokeball_rect2)   
            pygame.display.update()
            clock.tick(160)
    
          
    if variabile_di_stato=="game_over":
        run = True  
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            game_over_screen.blit(sfondo_game_over, (0,0))
            screen.blit(logo_image, (180,80))
            game_over.cliccare()
            if game_over.action():
                variabile_di_stato = "menu"
                print(variabile_di_stato)
            
            if variabile_di_stato == "menu":
                run = False
                break
                            
            print(variabile_di_stato)
                
            
            
            pygame.display.update()
            clock.tick(160)

