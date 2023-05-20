import pygame
from typing import Any
from random import randint
class Drago():
    def __init__(self, schermo, pos, size, screen):
        self.dragoRect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.dragoimage = pygame.image.load('image\drago-removebg-preview - Copia inv.png')
        self.dragoimage = pygame.transform.scale(self.dragoimage, size)
        self.schermo = schermo
        self.screen  = screen
        self.muovi_destra = False
        self.muovi_sinistra = False
        self.muovi_sopra = False
        self.muovi_sotto = False
        self.vel_vert = 10
        self.vel_orizz = 5
          
    
        
    def move_right(self):
        self.muovi_destra = True
        # self.muovi_sinistra = False
    def move_left(self):
        self.muovi_sinistra = True
        # self.muovi_destra = False
    def move_foward(self):
        self.muovi_sopra = True
        # self.muovi_sotto = False
    def move_back(self):
        self.muovi_sotto = True
        # self.muovi_sopra = False

    def stop_moving_right(self):
        self.muovi_destra = False
    def stop_moving_left(self):
        self.muovi_sinistra = False
    def stop_moving_foward(self):
        self.muovi_sopra = False
    def stop_moving_back(self):
        self.muovi_sotto = False

    def muovimento(self):
        
        if self.muovi_destra:   
            self.dragoRect.right += self.vel_orizz
            if self.dragoRect.right > self.screen.get_width():
                self.dragoRect.right = self.screen.get_width()
               
        if self.muovi_sinistra:
            self.dragoRect.left -= self.vel_orizz
            if self.dragoRect.left < 0:
                self.dragoRect.left = 0
                
        if self.muovi_sopra:
            self.dragoRect.top -= self.vel_vert
            if self.dragoRect.top < 0:
                self.dragoRect.top = 0
                

        if self.muovi_sotto:
            self.dragoRect.bottom += self.vel_vert
            if self.dragoRect.bottom > self.screen.get_height():
                self.dragoRect.bottom = self.screen.get_height()
    
    def disegna(self):
        self.screen.blit(self.dragoimage, self.dragoRect)
    


        







    

