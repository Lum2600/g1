
from typing import Any
import pygame     
class Personaggio:
    def __init__(self, screen, pos, size, BG_SIZE ) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('git_hub\immagini\drago-removebg-preview - Copia.png')
        self.image = pygame.transform.scale(self.image, size)
        self.vel = [0,0]
        self.moving_back = False
        self.moving_foward = False
        self.moving_right = False
        self.moving_left = False
        self.vel_vert = 10
        self.vel_orizz = 10
        
        
        
    
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
        
    def collide(self):
        if self.rect.midright == 900:
            return True
        else:
            return False
        # if self.rect.collidepoint(-display_x):
        #     self.screen+=self.vel_orizz






    
