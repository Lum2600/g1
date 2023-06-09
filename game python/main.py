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
sfondo_1 = pygame.image.load('image\sfondo_1.webp')
sfondo_1 = pygame.transform.scale(sfondo_1, (720, 1080))
sfondo_2 = pygame.image.load('image\sfondo_mappa2.jpg')
sfondo_2 = pygame.transform.scale(sfondo_2, (720, 1080))
sfondo_3 = pygame.image.load('image\sfondo_mappa3.jpg')
sfondo_3 = pygame.transform.scale(sfondo_3, (720, 1080))

#schermo del menu
menu_screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo_menu = pygame.image.load('image/sfondoy.png')
sfondo_menu = pygame.transform.scale(sfondo, (720, 1080))
logo_image= pygame.image.load('image\logo.png')



#schermo delle skin
skin_screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo_skin = pygame.image.load('image\sfondo_skin.png')
sfondo_skin= pygame.transform.scale(sfondo_skin, (720, 1080))

#schermo del gameover
game_over_screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo_game_over = pygame.image.load("image\sfondo_over.jpg")
sfondo_game_over = pygame.transform.scale(sfondo_game_over, (720, 1080))

#musica
ost = pygame.mixer.music.load("image\X2Download.app - 1 Hour of Relaxing Pokemon HeartGold_SoulSilver Music Compilation (128 kbps).mp3")
pygame.mixer_music.set_volume(1.0)
score_100 = pygame.mixer.Sound('image\Mario Jump Sound Effect.mp3')
death_music = pygame.mixer.Sound('image\The Legend of Zelda 25th Anniversary Symphony- Ballad of the Goddess (Skyward Sword).mp3')
game_over_sound = pygame.mixer.Sound('image\The sound of taking damage from an old game (Sound effect).mp3')


#costanti di gioco
vel_vert = 10
vel_orizz = 5
font = pygame.font.Font('image\Pokemon Classic.ttf', 25)
font2 = pygame.font.Font('image\Pokemon Classic.ttf', 25)
font3 = pygame.font.Font('image\Pokemon Classic.ttf', 17)
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
modalita = "facile"
skin_button_size = (150, 150)
variabile_personaggio = "c"
tick = 0
mossa = False

#immagini png
vite_image = pygame.image.load('image/Vite.png')
vite_rect = pygame.Rect((5, 5), (40, 40) )
vite_image = pygame.transform.scale(vite_image, (40, 40))
moneta_image1 = pygame.image.load('image/moneta-removebg-preview (1).png')
moneta_rect1 = pygame.Rect((randint(0, 450), 0), (80, 80) )
moneta_image1 = pygame.transform.scale(moneta_image1,(80, 80))
moneta_image2 = pygame.image.load('image/moneta-removebg-preview (1).png')
moneta_rect2 = pygame.Rect((randint(500, 630), -100), (80, 80) )
moneta_image2 = pygame.transform.scale(moneta_image1,(80, 80))
moneta_image3 = pygame.image.load('image/moneta-removebg-preview (1).png')
moneta_rect3= pygame.Rect((randint(0, 450), 0), (80, 80) )
moneta_image3 = pygame.transform.scale(moneta_image1,(80, 80))
moneta_image4 = pygame.image.load('image/moneta-removebg-preview (1).png')
moneta_rect4= pygame.Rect((randint(500, 630), -100), (80, 80) )
moneta_image4 = pygame.transform.scale(moneta_image1,(80, 80))
pokeball_image1 = pygame.image.load('image/pokeball.png')
pokeball_image2 =pygame.image.load('image/pokeball.png')
pokeball_rect1 = pygame.Rect((randint(0, 450), -100), (30, 30) )
pokeball_rect2 = pygame.Rect((randint(500, 660), -100), (30, 30) )
pokeball_image1 = pygame.transform.scale(pokeball_image1,(40, 40))
pokeball_image2 = pygame.transform.scale(pokeball_image2,(40, 40))
pokeball_image3 = pygame.image.load('image/pokeball.png')
pokeball_image4 =pygame.image.load('image/pokeball.png')
pokeball_rect3 = pygame.Rect((randint(0, 450), -100), (30, 30) )
pokeball_rect4 = pygame.Rect((randint(500, 660), -100), (30, 30) )
pokeball_image3 = pygame.transform.scale(pokeball_image3,(40, 40))
pokeball_image4 = pygame.transform.scale(pokeball_image4,(40, 40))



#skin

skin_charizard = pygame.image.load('image\drago-removebg-preview - Copia inv.png')
skin_charizard = pygame.transform.scale(skin_charizard, (100, 100))
skin_charizard_rect = pygame.Rect((10, 290), (skin_button_size))
info_c1 = font3.render('Charizard è un Pokémon competitivo.', True, (255, 255, 255))
info_c2 = font3.render('Ama la lotta e spende il suo tempo ad', True, (255, 255, 255))
info_c3 = font3.render('allenarsi e a cercare avversari.', True, (255, 255, 255))




skin_ven = pygame.image.load('image\skin_ven.png')
skin_ven = pygame.transform.scale(skin_ven, (100, 100))
skin_ven_rect = pygame.Rect((10, 530), (skin_button_size))
info_v1 = font3.render('Venusaur è una creatura quadrupede dalla pelle color verde acqua', True, (255, 255, 255))
info_v2 = font3.render('e ha tre grossi artigli su ogni zampa', True, (255, 255, 255))
info_v3 = font3.render('inoltre ha quattro zanne abbastanza', True, (255, 255, 255))
info_v4 = font3.render('evidenti nella mascella inferiore, oltre alle due su quella superiore.', True, (255, 255, 255))



skin_bul = pygame.image.load('image\skin_bul.png')
skin_bul = pygame.transform.scale(skin_bul, (100, 100))
skin_bul_rect = pygame.Rect((10, 765), (skin_button_size))
info_b1 = font3.render('Blastoise, ha le sembianze di una ', True, (255, 255, 255))
info_b2 = font3.render('tartaruga bipede dal colore', True, (255, 255, 255))
info_b3 = font3.render('prevalentemente blu', True, (255, 255, 255))
info_b4 = font3.render('e ha tre grossi artigli su ogni zampa', True, (255, 255, 255))
info_b5 = font3.render('apparentemente metallici da cui spara forti getti d acqua. ', True, (255, 255, 255))
info_b6 = font3.render('forti getti d acqua. ', True, (255, 255, 255))



def myFunction():
    print('Button Pressed')

#bottoni
start = oggetti.Button_start((250, 225, 2),screen, 98, 390, 250, 80, 'Start', myFunction)
skin = oggetti.Button_start((250, 225, 2),screen, 358, 390, 250, 80, 'Starter', myFunction)
dif_1 = oggetti.Button_dif(screen, 205, 500, 100, 80, '1', myFunction)
dif_2 = oggetti.Button_dif(screen, 310, 500, 100, 80, '2', myFunction)
dif_3 = oggetti.Button_dif(screen, 415, 500, 100, 80, '3', myFunction)
skin_1 = oggetti.Button_skin((255, 255, 255),screen, 10, 450, 150, 50, 'seleziona', myFunction)
skin_2 = oggetti.Button_skin((255, 225, 255),screen, 10, 690, 150, 50, 'seleziona', myFunction)
skin_3 = oggetti.Button_skin((255, 225, 255),screen, 10, 925, 150, 50, 'seleziona', myFunction)
conferma = oggetti.Button_start((255, 225, 255),screen, 10, 980, 700, 70, 'conferma', myFunction)
game_over = oggetti.Button_skin((255, 255, 255),screen, 280, 600, 150, 50, 'Riprova', myFunction)



#giocatore





while True:
    pygame.mixer.music.unpause()
    
    if variabile_di_stato == "skin":
        run = True
        while run:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            skin_screen.blit(schermo, ((skin_screen.get_width()-schermo.get_width())//2, (skin_screen.get_height()-schermo.get_height())//2 ))
            skin_screen.blit(sfondo_skin, (0,0))
            screen.blit(logo_image, (170,10))
            seleziona  = font2.render('! SELEZIONA IL TUO POKEMON !', True, (255, 255, 255))
            skin_screen.blit(seleziona, (35, 200))
            skin_1.cliccare()
            if skin_1.action():
                
                variabile_personaggio = 'c'
                
            skin_2.cliccare()
            if skin_2.action():
                
                variabile_personaggio = 'v'
                
            skin_3.cliccare()
            if skin_3.action():
                
                variabile_personaggio = 'b'
        
                
            conferma.cliccare()
            
                
                
            
            skin_screen.blit(skin_charizard, (35, 315))
            #pygame.draw.rect(skin_screen, 'black', skin_charizard_rect, 5)
            screen.blit(info_c1, (200, 300))
            screen.blit(info_c2, (200, 335))
            screen.blit(info_c3, (200, 370))
            
            skin_screen.blit(skin_ven, (35, 560))
            #pygame.draw.rect(skin_screen, 'black', skin_ven_rect, 5
            screen.blit(info_v1, (200, 565))
            screen.blit(info_v2, (200, 590))
            screen.blit(info_v3, (200, 620))
            screen.blit(info_v4, (200, 650))
            
            
            skin_screen.blit(skin_bul, (35, 790))
            screen.blit(info_b1, (200, 790))
            screen.blit(info_b2, (200, 815))
            screen.blit(info_b3, (200, 840))
            screen.blit(info_b4, (200, 865))
            screen.blit(info_b5, (200, 890))
            screen.blit(info_b6, (200, 915))
            #pygame.draw.rect(skin_screen, 'black', skin_bul_rect, 5)
            if conferma.action() :
                variabile_di_stato = "menu"
                
            
                
            if variabile_di_stato !="skin":
                    variabile_di_stato = 'menu'
                    pygame.display.update()
                    clock.tick(160)
                    # tick-=1
                    menu_screen.blit(sfondo_menu, (0,0))
                    run = False
                    tick+=1
                    
                

            pygame.display.update()
            clock.tick(160)
            break
    
    
    
    if variabile_di_stato=="menu":
        ost = pygame.mixer.music.load("image\X2Download.app - 1 Hour of Relaxing Pokemon HeartGold_SoulSilver Music Compilation (128 kbps).mp3")
        pygame.mixer.music.play(-1)
        
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
           
            
            screen.blit(logo_image, (170,100))
            start.cliccare()
            skin.cliccare()
            dif_1.cliccare("facile")
            dif_2.cliccare("media")
            dif_3.cliccare("difficile")
            if dif_1.action():
                    modalita = "facile"
                    mod_1 = font2.render('difficoltà :  facile', True, (255, 255, 255))
                    screen.blit(mod_1, (200, 900))
            if dif_2.action():
                    modalita = "media"
                    mod_2 = font2.render('difficoltà :  media', True, (255, 255, 255))
                    screen.blit(mod_2, (200, 900))
            if dif_3.action():
                    modalita = "difficile"
                    mod_3 = font2.render('difficoltà :  difficile', True, (255, 255, 255))
                    screen.blit(mod_3, (200, 900))
            variabile_di_stato = "menu"  
            
            if skin.action() :
                
                if tick%2==0:
                        variabile_di_stato = "skin"
                        break
            
            variabile_di_stato = 'menu'
            
            
            if start.action():
                variabile_di_stato = "gioco"
            if variabile_di_stato ==  "gioco":
                run = False
                break
            
            pygame.display.update()
            clock.tick(160)

    
    
    
    
    
    
    
    if variabile_di_stato =="gioco":
            pygame.mixer.Sound.stop(death_music)
            pygame.mixer.music.pause()
            score = 0
            ost = pygame.mixer.music.load("image\X2Download.app - 1 Hour of Relaxing Pokemon HeartGold_SoulSilver Music Compilation (128 kbps).mp3")
            pygame.mixer.music.play(-1)
            if variabile_personaggio == 'c':
                    personaggio_immagine = pygame.image.load("image\drago-removebg-preview - Copia inv.png")
                    drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)- 100) , (140, 140), screen, personaggio_immagine)
                    
                    

            if variabile_personaggio == 'v':
                    personaggio_immagine = pygame.image.load( "image\skin_ven.png")

                    drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen, personaggio_immagine)
            if variabile_personaggio == 'b':
                    personaggio_immagine = pygame.image.load( "image\skin_bul.png")
                    drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen, personaggio_immagine)
                
            run = True
            while run:
                
                
                    
                if modalita == "facile":
                    pygame.mixer.music.unpause()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == TIMERSHOT:
                            score+=incremento_al_sec
                            
              
                    keys = pygame.key.get_pressed()

                    if keys[K_m]:
                        
                        vel_monete = 0
                        vel_pokeball = 0
                        incremento_al_sec = 0
                        drago.pausa()
                
                    elif keys[K_n]: 
                        vel_pokeball = 1.8
                        vel_monete = 2.2
                        drago.btg()
                        incremento_al_sec = 1
                
                    elif keys[K_BACKSPACE]:
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
                    screen.blit(sfondo_1, (0, 0))

                    drago.muovimento()
                    drago.disegna()
            
                    if (score+1000)%1000== 0 and score!=0:
                        pygame.mixer.Sound.set_volume(score_100, 0.1)
                        pygame.mixer.Sound.play(score_100)
                

                    moneta_rect1.y+=vel_monete
                    if moneta_rect1.y > screen.get_height(): 
                        moneta_rect1.y = randint(-800, 0)
                        moneta_rect1.x = randint(0, 450)


                    moneta_rect2.y += vel_monete
                    if moneta_rect2.y > screen.get_height(): 
                        moneta_rect2.y = randint(-800, 0)
                        moneta_rect2.x = randint(500, 640)
                    
                    moneta_rect3.y+=vel_monete
                    if moneta_rect3.y > screen.get_height(): 
                        moneta_rect3.y = randint(-800, 0)
                        moneta_rect3.x = randint(0, 450)


                    moneta_rect4.y += vel_monete
                    if moneta_rect4.y > screen.get_height(): 
                        moneta_rect4.y = randint(-800, 0)
                        moneta_rect4.x = randint(500, 640)

                    pokeball_rect1.y += vel_pokeball
                    if pokeball_rect1.y > screen.get_height(): 
                        pokeball_rect1.y = randint(-800, 0)
                        pokeball_rect1.x = randint(0, 450)

                    pokeball_rect2.y += vel_pokeball
                    if pokeball_rect2.y > screen.get_height(): 
                        pokeball_rect2.y = randint(-800, 0)
                        pokeball_rect2.x = randint(500, 640)



                    if oggetti.collisione(moneta_rect1, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        moneta_rect1.y = randint(-800, 0)
                        moneta_rect1.x = randint(0, 450)
                        score +=10
                        
        
                    elif oggetti.collisione(moneta_rect2, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)

                        moneta_rect2.y = randint(-800, 0)
                        moneta_rect2.x = randint(500, 640)
                        score +=10
                    
                    elif oggetti.collisione(moneta_rect3, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        moneta_rect3.y = randint(-800, 0)
                        moneta_rect3.x = randint(0, 450)
                        score +=10
                        pygame.mixer.Sound.play(difficile)
        
                    elif oggetti.collisione(moneta_rect4, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        moneta_rect4.y = randint(-800, 0)
                        moneta_rect4.x = randint(500, 640)
                        score +=10
                        pygame.mixer.Sound.play(difficile)
        
        
                    elif oggetti.collisione(pokeball_rect1, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect1.y = randint(-800, 0)
                        pokeball_rect1.x = randint(0, 450)
                        num_collisioni+=1
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        
                    elif oggetti.collisione(pokeball_rect2, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect2.y = randint(-800, 0)
                        pokeball_rect2.x = randint(500, 640)
                        num_collisioni+=1
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
        
                    if num_collisioni == 0:
                        screen.blit(vite_image, (5, 5))
                        screen.blit(vite_image, (55, 5))
                        screen.blit(vite_image, (105, 5))
                    elif num_collisioni == 1:
                        screen.blit(vite_image, (5, 5))
                        screen.blit(vite_image, (55, 5))
                    elif num_collisioni == 2:
                        screen.blit(vite_image, (5, 5))
                    else:
                        variabile_di_stato = "game_over"
                        
                
                    if variabile_di_stato !="gioco":
                        pygame.mixer.Sound.set_volume(game_over_sound, 0.5)
                        pygame.mixer.Sound.play(game_over_sound)
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
                        drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen, personaggio_immagine)
                        num_collisioni = 0
                        run = False
                        break
                    

                    screen.blit(moneta_image1, moneta_rect1)
                    screen.blit(moneta_image2, moneta_rect2)
                    screen.blit(moneta_image3, moneta_rect3)
                    screen.blit(moneta_image4, moneta_rect4)
                    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                    screen.blit(score_text, (300, 10))
                    screen.blit(pokeball_image1, pokeball_rect1)
                    screen.blit(pokeball_image2, pokeball_rect2)   
                    pygame.display.update()
                    clock.tick(160)

                if modalita == "media":
                    pygame.mixer.music.unpause()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == TIMERSHOT:
                            score+=incremento_al_sec
                            
                
                    
            
                        
                    keys = pygame.key.get_pressed()

                    if keys[K_m]:
                        vel_monete = 0
                        vel_pokeball = 0
                        incremento_al_sec = 0
                        drago.pausa()
                
                    elif keys[K_n]: 
                        drago.btg()
                        incremento_al_sec = 1
                        vel_pokeball = 2.5
                        vel_monete = 2.2
                
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
                    screen.blit(sfondo_2, (0, 0))
                    drago.muovimento()
                    drago.disegna()
            
                    if (score+1000)%1000== 0 and score!=0:
                        pygame.mixer.Sound.set_volume(score_100, 0.1)
                        pygame.mixer.Sound.play(score_100)

       
                

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
                    
                    pokeball_rect3.y += vel_pokeball
                    if pokeball_rect3.y > screen.get_height(): 
                        pokeball_rect3.y = randint(-800, 0)
                        pokeball_rect3.x = randint(0, 450)
                    
                    pokeball_rect4.y += vel_pokeball
                    if pokeball_rect4.y > screen.get_height(): 
                        pokeball_rect4.y = randint(-800, 0)
                        pokeball_rect4.x = randint(500, 640)
                    
                    



                    if oggetti.collisione(moneta_rect1, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        moneta_rect1.y = randint(-800, 0)
                        moneta_rect1.x = randint(0, 450)
                        score +=10
                        pygame.mixer.Sound.play(difficile)
            
                    elif oggetti.collisione(moneta_rect2, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        moneta_rect2.y = randint(-800, 0)
                        moneta_rect2.x = randint(500, 640)
                        score +=10
                        pygame.mixer.Sound.play(difficile)
            
            
                    elif oggetti.collisione(pokeball_rect1, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect1.y = randint(-800, 0)
                        pokeball_rect1.x = randint(0, 450)
                        num_collisioni+=1
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        
                    elif oggetti.collisione(pokeball_rect2, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect2.y = randint(-800, 0)
                        pokeball_rect2.x = randint(500, 640)
                        num_collisioni+=1
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                    
                    elif oggetti.collisione(pokeball_rect3, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect3.y = randint(-800, 0)
                        pokeball_rect3.x = randint(0, 450)
                        num_collisioni+=1
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
            
                    elif oggetti.collisione(pokeball_rect4, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect4.y = randint(-800, 0)
                        pokeball_rect4.x = randint(500, 640)
                        num_collisioni+=1
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
            
                    if keys[K_q]:
                            mossa = True
                    
                    
                    if mossa ==True:
                        pokeball_rect1.y = -100
                        pokeball_rect2.y = -100
                        pygame.time.delay(10)
                        screen.fill((255, 255, 255))
                        
                        screen.fill((255, 0, 0))
                        pygame.time.delay(300)
                        screen.fill((255, 255, 255))
                        pygame.time.delay(300)
                        screen.fill((255, 0, 0))
                        
                        mossa = False
                    
            
                    if num_collisioni == 0:
                        screen.blit(vite_image, (5, 5))
                        screen.blit(vite_image, (55, 5))
                        screen.blit(vite_image, (105, 5))
                    elif num_collisioni == 1:
                        screen.blit(vite_image, (5, 5))
                        screen.blit(vite_image, (55, 5))
                    elif num_collisioni == 2:
                        screen.blit(vite_image, (5, 5))
                    else:
                        variabile_di_stato = "game_over"
                        
                    
                    if variabile_di_stato !="gioco":
                        variabile_di_stato = 'game_over'
                        pygame.mixer.Sound.set_volume(game_over_sound, 0.5)
                        pygame.mixer.Sound.play(game_over_sound)
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
                        drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen, personaggio_immagine)
                        num_collisioni = 0
                        run = False
                        break
                    

                    screen.blit(moneta_image1, moneta_rect1)
                    screen.blit(moneta_image2, moneta_rect2)
                    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                    screen.blit(score_text, (300, 10))
                    screen.blit(pokeball_image1, pokeball_rect1)
                    screen.blit(pokeball_image2, pokeball_rect2)
                    screen.blit(pokeball_image3, pokeball_rect3)
                    screen.blit(pokeball_image4, pokeball_rect4)  
                    pygame.display.update()
                    clock.tick(160)
                if modalita == "difficile":
                    
                    

                    
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == TIMERSHOT:
                            score+=incremento_al_sec
                           
                
                    
            
                        
                    keys = pygame.key.get_pressed()

                    if keys[K_m]:
                        vel_monete = 0
                        vel_pokeball = 0
                        incremento_al_sec = 0
                        drago.pausa()
                
                    elif keys[K_n]: 
                        drago.btg()
                        incremento_al_sec = 1
                        vel_pokeball = 2.0
                        vel_monete = 1.6  
                
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
                    screen.blit(sfondo_3, (0, 0))
                    drago.muovimento()
                    drago.disegna()
            
                    if (score+1000)%1000== 0 and score!=0:
                        pygame.mixer.Sound.set_volume(score_100, 0.1)
                        pygame.mixer.Sound.play(score_100)

                    if keys[K_q]:
                            mossa = True
                    
                    
                    if mossa ==True:
                        pokeball_rect1.y = -100
                        pokeball_rect2.y = -100
                        pygame.time.delay(10)
                        screen.fill((255, 255, 255))
                        
                        screen.fill((255, 0, 0))
                        pygame.time.delay(300)
                        screen.fill((255, 255, 255))
                        pygame.time.delay(300)
                        screen.fill((255, 0, 0))
                        
                        mossa = False

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
                        if vel_pokeball<5:
                            vel_pokeball+=0.1

                    pokeball_rect2.y += vel_pokeball
                    if pokeball_rect2.y > screen.get_height(): 
                        pokeball_rect2.y = randint(-800, 0)
                        pokeball_rect2.x = randint(500, 640)
                        if vel_pokeball<5:
                            vel_pokeball+=0.1

                    
                    pokeball_rect3.y += vel_pokeball
                    if pokeball_rect3.y > screen.get_height(): 
                        pokeball_rect3.y = randint(-800, 0)
                        pokeball_rect3.x = randint(0, 450)
                        if vel_pokeball<5:
                            vel_pokeball+=0.1

                    
                    pokeball_rect4.y += vel_pokeball
                    if pokeball_rect4.y > screen.get_height(): 
                        pokeball_rect4.y = randint(-800, 0)
                        pokeball_rect4.x= randint(500, 640)
                        if vel_pokeball<5:
                            vel_pokeball+=0.1

                    
                    



                    if oggetti.collisione(moneta_rect1, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        moneta_rect1.y = randint(-800, 0)
                        moneta_rect1.x = randint(0, 450)
                        score +=10
            
                    elif oggetti.collisione(moneta_rect2, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2Download.app - Ding Sound Effect (128 kbps).mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        moneta_rect2.y = randint(-800, 0)
                        moneta_rect2.x = randint(500, 640)
                        score +=10
            
            
                    elif oggetti.collisione(pokeball_rect1, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        pokeball_rect1.y = randint(-800, 0)
                        pokeball_rect1.x = randint(0, 450)
                        num_collisioni+=1
                    elif oggetti.collisione(pokeball_rect2, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        pokeball_rect2.y = randint(-800, 0)
                        pokeball_rect2.x = randint(500, 640)
                        num_collisioni+=1
                    
                    elif oggetti.collisione(pokeball_rect3, oggetti.Drago.returna_rect(drago)):
                        pokeball_rect3.y = randint(-800, 0)
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        pokeball_rect3.x = randint(0, 450)
                        num_collisioni+=1
            
                    elif oggetti.collisione(pokeball_rect4, oggetti.Drago.returna_rect(drago)):
                        difficile = pygame.mixer.Sound('image\X2downloadapp-super-effective-pokemon-sound-effects-128-kbps_yc7NsKAf.mp3')
                        pygame.mixer.Sound.set_volume(difficile, 1.0)
                        pygame.mixer.Sound.play(difficile)
                        pokeball_rect4.y = randint(-800, 0)
                        pokeball_rect4.x = randint(500, 640)
                        num_collisioni+=1
            
            
                    
            
                    if num_collisioni == 0:
                        screen.blit(vite_image, (5, 5))
                        screen.blit(vite_image, (55, 5))
                        screen.blit(vite_image, (105, 5))
                    elif num_collisioni == 1:
                        screen.blit(vite_image, (5, 5))
                        screen.blit(vite_image, (55, 5))
                    elif num_collisioni == 2:
                        
                        screen.blit(vite_image, (5, 5))
                    elif num_collisioni==3:
                        variabile_di_stato = "game_over"
                        
                    
                    if variabile_di_stato =="game_over":
                        variabile_di_stato = "game_over"
                        pygame.mixer.Sound.set_volume(game_over_sound, 0.5)
                        pygame.mixer.Sound.play(game_over_sound)
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
                        drago = oggetti.Drago(schermo, ((screen.get_width()//2), (schermo.get_height()//2)) , (140, 140), screen, personaggio_immagine)
                        num_collisioni = 0
                        moneta_rect1.y=randint(-800, 0)
                        moneta_rect2.y=randint(-800, 0)
                        pokeball_rect2.y=randint(-800, 0)
                        pokeball_rect3.y=randint(-800, 0)
                        pokeball_rect1.y=randint(-800, 0)
                        pokeball_rect4.y=randint(-800, 0)

                        run = False
                        
                        break
                    

                    screen.blit(moneta_image1, moneta_rect1)
                    screen.blit(moneta_image2, moneta_rect2)
                    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                    screen.blit(score_text, (300, 10))
                    screen.blit(pokeball_image1, pokeball_rect1)
                    screen.blit(pokeball_image2, pokeball_rect2)
                    screen.blit(pokeball_image3, pokeball_rect3)
                    screen.blit(pokeball_image4, pokeball_rect4)  
                    pygame.display.update()
                    clock.tick(160)
                
          
    if variabile_di_stato=="game_over":
        
        pygame.time.delay(200)
        pygame.mixer.music.pause()
        pygame.mixer.Sound.set_volume(death_music, 1.0)
        pygame.mixer.Sound.play(death_music)
        run = True  
        while run:
            
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            game_over_screen.blit(sfondo_game_over, (0,0))
            screen.blit(logo_image, (170,80))
            sconfitta = font2.render('Hai perso !', True, (255, 255, 255))
            sfonfitta_2 = font2.render(f'Il tuo punteggio è di {score}', True, (255, 255, 255))
            screen.blit(sconfitta, (100, 350))
            screen.blit(sfonfitta_2, (100, 400))
            game_over.cliccare()
            if game_over.action():
                variabile_di_stato = "gioco"
                
            if variabile_di_stato == "gioco":
                
                run = False
                
                break
                            
                
            
            
            pygame.display.update()
            clock.tick(160)

