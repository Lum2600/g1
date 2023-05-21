import pygame
import os 

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("First Game!")

WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (200, 250, 255)

BORDER = pygame.Rect(1000/2, 0, 10, 800)

FPS = 70
VEL = 5
COIN1_VEL = 3
COIN2_VEL = 5
COIN3_VEL = 4
COIN4_VEL = 3
COIN5_VEL = 6
COIN6_VEL = 3

# GRASS4_VEL = 3


FOX_IMAGE = pygame.image.load(os.path.join('image', 'fox.png'))
FOX = pygame.transform.rotate(pygame.transform.scale(FOX_IMAGE, (105, 105)), -5)

STAR_IMAGE = pygame.image.load(os.path.join('image', 'star.png'))
STAR = pygame.transform.scale(STAR_IMAGE, (80, 80))

GRASS_IMAGE = pygame.image.load(os.path.join('image', 'grass.png'))
GRASS1 = pygame.transform.scale(GRASS_IMAGE, (175, 175))
GRASS2 = pygame.transform.scale(GRASS_IMAGE, (175, 175))
GRASS3 = pygame.transform.scale(GRASS_IMAGE, (175, 175))
GRASS4 = pygame.transform.scale(GRASS_IMAGE, (175, 175))
GRASS5 = pygame.transform.scale(GRASS_IMAGE, (175, 175))

CLOUD_IMAGE = pygame.image.load(os.path.join('image', 'cloud.png'))
CLOUD1 = pygame.transform.scale(CLOUD_IMAGE, (190, 150))
CLOUD2 = pygame.transform.scale(CLOUD_IMAGE, (190, 150))
CLOUD3 = pygame.transform.scale(CLOUD_IMAGE, (190, 150))
CLOUD4 = pygame.transform.scale(CLOUD_IMAGE, (170, 120))
CLOUD5 = pygame.transform.scale(CLOUD_IMAGE, (170, 120))





COIN_IMAGE = pygame.image.load(os.path.join('image', 'coin.png'))
COIN = pygame.transform.scale(COIN_IMAGE, (50, 50))

TIME_IMAGE = pygame.image.load(os.path.join('image', 'time.png'))
TIME = pygame.transform.scale(TIME_IMAGE, (90, 30))



def draw_window(fox, star, grass1, grass2, grass3, grass4, grass5, cloud1, cloud2, cloud3, cloud4, cloud5, coin1, coin2, coin3, coin4, coin5, coin6, time, time1):
    WIN.fill((100, 180, 215))
    pygame.draw.rect(WIN, BLUE, BORDER)
    WIN.blit(FOX, (fox.x, fox.y))
    WIN.blit(STAR,(star.x, star.y))
    WIN.blit(COIN,(coin1.x, coin1.y))
    WIN.blit(COIN,(coin2.x, coin2.y))
    WIN.blit(COIN,(coin3.x, coin3.y))
    WIN.blit(COIN,(coin4.x, coin4.y))
    WIN.blit(COIN,(coin5.x, coin5.y))
    WIN.blit(COIN,(coin6.x, coin6.y))
    WIN.blit(GRASS1,(grass1.x, grass1.y))
    WIN.blit(GRASS2,(grass2.x, grass2.y))
    WIN.blit(GRASS3,(grass3.x, grass3.y))
    WIN.blit(GRASS4,(grass4.x, grass4.y))
    WIN.blit(GRASS5,(grass5.x, grass5.y))
    WIN.blit(CLOUD1,(cloud1.x, cloud1.y))
    WIN.blit(CLOUD2,(cloud2.x, cloud2.y))
    WIN.blit(CLOUD3,(cloud3.x, cloud3.y))
    WIN.blit(CLOUD4,(cloud4.x, cloud4.y))
    WIN.blit(CLOUD5,(cloud5.x, cloud5.y))
    
    WIN.blit(TIME,(time1.x, time1.y))
    WIN.blit(TIME,(time.x, time.y))
    
    pygame.display.update()




def fox_movement(keys_pressed, fox):
    
    if keys_pressed[pygame.K_1] and fox.x - VEL > BORDER.x: 
                fox.x -= VEL
    if keys_pressed[pygame.K_2] and fox.x - VEL + fox.width < 990: 
                fox.x += VEL
    if keys_pressed[pygame.K_3] and fox.y - VEL > 0: 
                fox.y -= VEL
    if keys_pressed[pygame.K_4] and fox.y + VEL + fox.height < 800 : 
                fox.y += VEL
                
def star_movement(keys_pressed, star):
    
    if keys_pressed[pygame.K_LEFT]and star.x + VEL > 0: 
                star.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and star.x + VEL +  star.width < BORDER.x: 
                star.x += VEL
    if keys_pressed[pygame.K_UP] and star.y - VEL > 0: 
                star.y -= VEL
    if keys_pressed[pygame.K_DOWN] and star.y + VEL + star.height < 800: 
                star.y += VEL
    
    
# def coin_movement(keys_pressed, coin):
#     if keys_pressed[pygame.K_0]:
#         coin.y += COIN_VEL

def main():
    
    fox = pygame.Rect(850, 0, 105, 105)
    star = pygame.Rect(0, 0, 80, 80)
    
    grass1 = pygame.Rect(-30, 45, 175, 175)
    grass2 = pygame.Rect(350, 280, 175, 175)
    grass3 = pygame.Rect(-30, 550, 175, 175)
    grass4 = pygame.Rect(175, 150, 175, 175)
    grass5 = pygame.Rect(175, 450, 175, 175)
    
    cloud1 = pygame.Rect(838, 80, 190, 150)
    cloud2 = pygame.Rect(838, 560, 190, 150)
    cloud3 = pygame.Rect(505, 300, 190, 150)
    cloud4 = pygame.Rect(680, 170, 190, 150)
    cloud5 = pygame.Rect(680, 450, 190, 150)
    
    coin1 = pygame.Rect(255, 0, 50, 50)
    coin2 = pygame.Rect(50, 0, 50, 50)
    coin3 = pygame.Rect(455, 0, 50, 50)
    coin4 = pygame.Rect(655, 0, 50, 50)
    coin5 = pygame.Rect(955, 0, 50, 50)
    coin6 = pygame.Rect(555, 0, 50, 50)
    
    time = pygame.Rect(400,0, 90, 30)
    time1 = pygame.Rect(520,0, 90, 30)
    clock= pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        fox_movement(keys_pressed, fox)
        star_movement(keys_pressed, star)

        
    
        coin1.y += COIN1_VEL
        if coin1.y > 750: coin1.y = 0
        coin2.y += COIN2_VEL
        if coin2.y > 750: coin2.y = 0
        coin3.y += COIN3_VEL
        if coin3.y > 750: coin3.y = 0
        coin4.y += COIN5_VEL
        if coin4.y > 750: coin4.y = 0
        coin5.y += COIN4_VEL
        if coin5.y > 750: coin5.y = 0
        coin6.y += COIN6_VEL
        if coin6.y > 750: coin6.y = 0
        # grass4.x += GRASS4_VEL
        # if GRASS4_VEL > 350:
        #     grass4.x -= GRASS4_VEL 
        # grass4.x -= GRASS4_VEL
        # if GRASS4_VEL == 0:
        #     grass4.x += GRASS4_VEL
        # if grass4.x < 0:
        #     grass4.x += GRASS4_VEL 
        # else: grass4.x -= GRASS4_VEL     
        # if grass4.x > 350: grass4.x = 0
                
        draw_window(fox, star, grass1, grass2, grass3, grass4, grass5, cloud1, cloud2, cloud3, cloud4, cloud5, coin1, coin2, coin3, coin4, coin5, coin6, time, time1)
            
    pygame.quit()
    
if __name__ == "__main__":
    main()