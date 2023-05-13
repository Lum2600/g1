
from typing import Any
import pygame   

class sfondo:
        def __init__(self, screen, pos, size) -> None:
            self.screen = screen
            self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
            self.image = pygame.image.load('git_hub\immagini\grass-removebg-preview.png')
            self.image = pygame.transform.scale(self.image, size)
            self.moving_back = False
            self.moving_foward = False
            self.moving_right = False
            self.moving_left = False
            self.vel_vert = 3
            self.vel_orizz = 3

        def muove_bg_back(self):
            self.moving_back = True
        def muove_bg_foward(self):
            self.moving_foward = True
        def muove_bg_left(self):
            self.moving_left = True
        def muove_bg_right(self):
            self.moving_right = True
        def stop_moving_left(self):
            self.moving_left = False
        def stop_moving_right(self):
            self.moving_right = False
        def stop_moving_foward(self):
            self.moving_foward = False
        def stop_moving_back(self):
            self.moving_back = False
        def muovi(self):
        
            if self.move_right():   
                self.rect.right += self.vel_orizz
                if self.rect.right > self.screen.get_width():
                    self.rect.right = self.screen.get_width()
                
               
            if self.move_left():
                self.rect.left -= self.vel_orizz
                if self.rect.left < 0:
                    self.rect.left = 0
                
                
            if self.move_foward():
                self.rect.top -= self.vel_vert
                if self.rect.top < 0:
                    self.rect.top = 0
                

            if self.move_back():
                self.rect.top += self.vel_vert
                if self.rect.bottom > self.screen.get_height():
                    self.rect.bottom = self.screen.get_height()
                
        def draw(self):
            self.screen.blit(self.image, self.rect)
            

from typing import Any
import pygame     
class Personaggio:
    def __init__(self, screen, pos, size ) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('git_hub\immagini\drago-removebg-preview - Copia.png')
        self.image = pygame.transform.scale(self.image, size)
        self.vel = [0,0]
        self.moving_back = False
        self.moving_foward = False
        self.moving_right = False
        self.moving_left = False
        self.vel_vert = 3
        self.vel_orizz = 3
        self.col_back = False
        self.col_foward = False
        self.col_left = False
        self.col_right = False
        
        
    
    def move_right(self):
        self.moving_right = True
        self.moving_left = False
        
        
        
    
    def stop_moving_right(self):
        self.moving_right = False
        

    def move_left(self):
        self.moving_left = True
        self.moving_right = False
       
    
    def stop_moving_left(self):
        self.moving_left = False
       

    def move_foward(self):
        self.moving_foward = True
        self.moving_down = False
    
    def stop_moving_foward(self):
        self.moving_foward = False
            


    def move_back(self):
        self.moving_back = True
        self.moving_foward = False

    def stop_moving_back(self):
        self.moving_back = False

    def coll_right(self):
        self.col_right = True
    def coll_left(self):
        self.coll_left= True
    def coll_foward(self):
        self.col_foward = True
    def coll_back(self):
        self.col_back = True


    def muovi(self):
        


        # collisione col pavimento
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            self.vel[1] = 0
           
        # muovi
        if self.moving_right:   
            self.image = pygame.image.load('git_hub\immagini\drago-removebg-preview - Copia inv.png')
            self.rect.right += self.vel_orizz
            if self.rect.right > self.screen.get_width():
                self.rect.right = self.screen.get_width()
               
        if self.moving_left:
            self.image = pygame.image.load('git_hub\immagini\drago-removebg-preview - Copia.png')
            self.rect.left -= self.vel_orizz
            if self.rect.left < 0:
                self.rect.left = 0
                
        if self.moving_foward:
            self.rect.top -= self.vel_vert
            if self.rect.top < 0:
                self.rect.top = 0
                

        if self.moving_back:
            
            self.rect.top += self.vel_vert
            if self.rect.bottom > self.screen.get_height():
                self.rect.bottom = self.screen.get_height()
                

    def draw(self):
        self.screen.blit(self.image, self.rect)




class bush:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('git_hub\immagini\bush-removebg-preview.png')
        self.image = pygame.transform.scale(self.image, size)
    def draw(self):
        self.screen.blit(self.image, self.rect)

    
