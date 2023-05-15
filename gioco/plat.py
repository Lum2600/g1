import pygame
from math import ceil

class Piattaforma():
    def __init__(self, display, nomefile = 'git_hub\gioco\mappe\mappa1.txt') -> None:
        self.display = display
        self.grass_image = pygame.image.load('git_hub\immagini\grass-removebg-preview.png')
        self.dirt_image = pygame.image.load('git_hub\immagini\Buhs and grass.jpeg')
        self.street_image = pygame.image.load('git_hub\immagini\dirt.jpeg')
        self.street_image_sx = pygame.image.load('git_hub\immagini\dirt_sx.jpeg')
        self.street_image_dx = pygame.image.load('git_hub\immagini\dirt_dx.jpeg')
        self.vel_vert = 10
        self.vel_orizz = 10
        with open(nomefile) as f:
            self.game_map = [list(map(int, riga.strip().split())) for riga in f]
        self.num_rows = len(self.game_map)
        self.num_cols = len(self.game_map)
        self.tile_width = ceil(display.get_width() / ((self.num_cols) + 1))
        self.tile_height = ceil(display.get_height() / self.num_rows) 
        self.grass_image = pygame.transform.scale(self.grass_image, (self.tile_width, self.tile_height))
        self.dirt_image = pygame.transform.scale(self.dirt_image, (self.tile_width, self.tile_height))
        self.street_image = pygame.transform.scale(self.street_image, (self.tile_width, self.tile_height))
        self.street_image_sx = pygame.transform.scale(self.street_image_sx, (self.tile_width, self.tile_height))
        self.street_image_dx = pygame.transform.scale(self.street_image_dx, (self.tile_width, self.tile_height))
        self.tile_rects = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile != 0:
                    self.tile_rects.append(pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height))
    
    def draw(self):
        self.display.fill((46,244,255))
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.display.blit(self.dirt_image, (x * self.tile_width, y * self.tile_height) )
                if tile == 2:
                    self.display.blit(self.dirt_image, (x * self.tile_width, y * self.tile_height) )
                    self.display.blit(self.grass_image, (x * self.tile_width, y * self.tile_height))
                if tile == 3:
                    self.display.blit(self.street_image, (x * self.tile_width, y * self.tile_height))
                if tile == 4:
                    self.display.blit(self.street_image_dx, (x * self.tile_width, y * self.tile_height))
                if tile == 5:
                    self.display.blit(self.street_image_sx, (x * self.tile_width, y * self.tile_height))   

    def move_sx(self):
        self.display-=self.vel_orizz