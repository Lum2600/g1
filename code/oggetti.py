import pygame
from typing import Any
import sys
from random import randint
pygame.font.init()
class Drago():
    def __init__(self, schermo, pos, size, screen):
        self.dragoRect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.dragoimage = pygame.image.load('image/drago-removebg-preview - Copia inv.png')
        self.dragoimage = pygame.transform.scale(self.dragoimage, size)
        self.schermo = schermo
        self.screen  = screen
        self.muovi_destra = False
        self.muovi_sinistra = False
        self.muovi_sopra = False
        self.muovi_sotto = False
        self.vel_vert = 1.7
        self.vel_orizz = 1.7
          
    
        
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
            self.dragoimage = pygame.image.load('image/drago-removebg-preview - Copia inv.png')
            if self.dragoRect.right > self.screen.get_width():
                self.dragoRect.right = self.screen.get_width()
               
        if self.muovi_sinistra:
            self.dragoimage = pygame.image.load('image\drago-removebg-preview.png')
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
    def returna_rect(self):
        return self.dragoRect
    def pausa(self):
        self.vel_orizz = 0
        self.vel_vert = 0
    def btg(self):
        self.vel_vert = 1.7
        self.vel_orizz = 1.7

    

def collisione_moneta1(moneta1, drago):
    if drago.colliderect(moneta1):
        return True
    
def collisione_moneta2(moneta2, drago):
    if drago.colliderect(moneta2):
        return True
    
def collisione_pokeball1(pokeball1, drago):
    if pokeball1.colliderect(drago):
        return True
    
def collisione_pokeball2(pokeball2, drago):
    if drago.colliderect(pokeball2):
        return True



font = pygame.font.SysFont('Arial', 40)
class Button():
    def __init__(self,bg_color,screen, x, y, width, height, buttonText='Button', cliccami=None, uno=False):
        self.x = x
        self.y = y
        self.bg_color=bg_color
        self.width = width
        self.height = height
        self.cliccato = cliccami
        self.stai_cliccando = uno
        self.schiacciato = False
        self.screen = screen
        self.image = pygame.image.load('image/lgo-removebg-preview.png')
        self.image = pygame.transform.scale(self.image, (350, 150))
        self.colora = {
            'normale': self.bg_color,
            'sopra mouse': '#666666',
            'schiacciato': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        self.bottoni = []
        self.bottoni.append(self)
    

        
    def cliccare(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.colora['normale'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.colora['sopra mouse'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.colora['schiacciato'])
                
                self.schiacciato = True
                self.cliccato()
                
            else:
                self.schiacciato = False

        self.buttonSurface.blit(self.buttonSurf, ((self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2), (self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2)))
        self.screen.blit(self.buttonSurface, self.buttonRect)
        
    def action(self):
        if self.schiacciato:
            return True
    def logo(self):
        self.screen.blit(self.image, (180, 100))