import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
import time
import sys

pygame.init()

pygame.display.set_caption("Platformer")

# Kleuren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Lettertype
font = pygame.font.Font(None, 74)

WIDTH, HEIGHT = 1280, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))

def toggle_fullscreen(window):
    current_flags = window.get_flags()
    if current_flags & pygame.FULLSCREEN:
        pygame.display.set_mode((WIDTH, HEIGHT))  # Venstermodus
    else:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # Fullscreen modus

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites
    
    return all_sprites

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_block2(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 64, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_block3(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 128, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_block_small(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(144, 0, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_block_small2(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(144, 64, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_block_small3(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(144, 128, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_bricks(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 64, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_bricks_small(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(320, 64, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_brown_stone_wide(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 0, size, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_brown_stone_small(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 16, size // 3, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_brown_stone(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(208, 16, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_brown_stone_high(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(240, 0, size // 3, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_brown_stone_jump(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 16, size, size // 12 * 1.25)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_stone_wide(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 64, size, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_stone_small(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 80, size // 3, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_stone(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(208, 80, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_stone_high(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(240, 64, size // 3, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_stone_jump(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 32, size, size // 12 * 1.25)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_stone_hole(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_wood_hole(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 64, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_leaves_hole(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 128, size, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_orange_stone_wide(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 128, size, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_orange_stone_small(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 144, size // 3, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_orange_stone(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(208, 144, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_orange_stone_high(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(240, 128, size // 3, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_gold_wide(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 128, size, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_gold_small(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 144, size // 3, size // 3)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_gold(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(288, 144, size // 3 * 2, size // 3 * 2)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_gold_high(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(320, 128, size // 3, size)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_gold_jump(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 0, size, size // 12 * 1.25)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_dirt(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    
    # Define the part of the image that has the "dirt" texture (skip the grass part)
    dirt_rect = pygame.Rect(96, 16, size, size - 16)  # Skip the top 16px of grass
    dirt_rect2 = pygame.Rect(96, 16, size, size - 80) 
    
    # Blit the dirt texture into the surface, starting after the grass layer
    surface.blit(image, (0, 16), dirt_rect)  # Position at y=16 to avoid the grass part
    
    # Add the top 16 pixels from Block, excluding the grass part (i.e. get the next 16px after grass)
    top_rect = pygame.Rect(96, 0, size, 1)  # Top strip for Dirt (excluding the grass)
    surface.blit(image, (0, 0), top_rect)  # Position this at the top of the surface
    
    # Fill the surface with the selected part of the dirt texture
    for y in range(1, 2):
        surface.blit(image, (0, y), dirt_rect2)  # Repeatedly blit the texture until the surface is full
    
    # Add the bottom strip (same logic as top, to complete the block appearance)
    bottom_rect = pygame.Rect(96, 32, size, 16)  # Bottom strip (mimicking Block)
    surface.blit(image, (0, size - 16), bottom_rect)  # Position this at the bottom of the surface
    
    return pygame.transform.scale2x(surface)

def get_dirt2(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    
    # Define the part of the image that has the "dirt" texture (skip the grass part)
    dirt_rect = pygame.Rect(96, 80, size, size - 16)  # Skip the top 16px of grass
    dirt_rect2 = pygame.Rect(96, 80, size, size - 80) 
    
    # Blit the dirt texture into the surface, starting after the grass layer
    surface.blit(image, (0, 16), dirt_rect)  # Position at y=16 to avoid the grass part
    
    # Add the top 16 pixels from Block, excluding the grass part (i.e. get the next 16px after grass)
    top_rect = pygame.Rect(96, 64, size, 1)  # Top strip for Dirt (excluding the grass)
    surface.blit(image, (0, 0), top_rect)  # Position this at the top of the surface
    
    # Fill the surface with the selected part of the dirt texture
    for y in range(1, 2):
        surface.blit(image, (0, y), dirt_rect2)  # Repeatedly blit the texture until the surface is full
    
    # Add the bottom strip (same logic as top, to complete the block appearance)
    bottom_rect = pygame.Rect(96, 96, size, 16)  # Bottom strip (mimicking Block)
    surface.blit(image, (0, size - 16), bottom_rect)  # Position this at the bottom of the surface
    
    return pygame.transform.scale2x(surface)

def get_dirt3(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    
    # Define the part of the image that has the "dirt" texture (skip the grass part)
    dirt_rect = pygame.Rect(96, 144, size, size - 16)  # Skip the top 16px of grass
    dirt_rect2 = pygame.Rect(96, 144, size, size - 80) 
    
    # Blit the dirt texture into the surface, starting after the grass layer
    surface.blit(image, (0, 16), dirt_rect)  # Position at y=16 to avoid the grass part
    
    # Add the top 16 pixels from Block, excluding the grass part (i.e. get the next 16px after grass)
    top_rect = pygame.Rect(96, 128, size, 1)  # Top strip for Dirt (excluding the grass)
    surface.blit(image, (0, 0), top_rect)  # Position this at the top of the surface
    
    # Fill the surface with the selected part of the dirt texture
    for y in range(1, 2):
        surface.blit(image, (0, y), dirt_rect2)  # Repeatedly blit the texture until the surface is full
    
    # Add the bottom strip (same logic as top, to complete the block appearance)
    bottom_rect = pygame.Rect(96, 160, size, 16)  # Bottom strip (mimicking Block)
    surface.blit(image, (0, size - 16), bottom_rect)  # Position this at the bottom of the surface
    
    return pygame.transform.scale2x(surface)

def get_coin(size):
    path = join("assets", "Items","Coin", "coin.png")
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (35, 35))
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size)
    surface.blit(image, (0, 0), rect)

    return surface

def get_finish_cup(size):
    path = join("assets", "Items", "Checkpoints", "End", "End (Idle).png")
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (64, 64))
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(9, 20, 46, 44)
    surface.blit(image, (0, 0), rect)

    return surface

def get_spikes(size):
    path = join("assets", "Traps", "Spikes", "idle.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 8, size // 3, size // 6)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(surface)

def get_spikes_down(size):
    path = join("assets", "Traps", "Spikes", "idle.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size // 3, size // 6)
    surface.blit(image, (0, 0), rect)

    return pygame.transform.scale2x(pygame.transform.rotate(surface, 180))

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "right"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.lives = 3  # Stel het aantal levens in
        self.hits = 0 # Telt het aantal hits op de speler
        self.last_hit_time = 0 # Houdt bij wanneer de laatste hit plaatsvond
        self.hit_cooldown = 2  # Stel de cooldown-tijd in seconden in
        self.score = 0
        self.last_score_update = 0
        self.is_gravity_active = True  # Vlag om te controleren of de zwaartekracht actief is

        self.heart_image = pygame.image.load(join("assets", "Other", "Heart.png")).convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (40, 40))  # Pas grootte aan indien nodig

        self.coin_image = pygame.image.load(join("assets", "Items","Coin", "coin.png")).convert_alpha()
        self.coin_image = pygame.transform.scale(self.coin_image, (35, 35))  # Pas grootte aan indien nodig
    
    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def scores(self):
        self.score += 1
        self.last_score_update = time.time()

    def make_hit(self):
        self.hit = True

        current_time = time.time()
        # Controleer of genoeg tijd is verstreken sinds de laatste hit
        if current_time - self.last_hit_time >= self.hit_cooldown:
            self.hits += 1
            self.last_hit_time = current_time  # Reset de timer voor de volgende hit
            
            if self.hits == 1:  # Verlies een leven na 3 hits
                self.lives -= 1
                self.hits = 0   # Reset het aantal hits na een leven te verliezen
                print("Een leven verloren! Aantal resterende levens:", self.lives)
                
                if self.lives == 0:
                    global game_over
                    game_over = True
       
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        if self.is_gravity_active:  # Controleer of de zwaartekracht actief is
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0 and self.is_gravity_active == True:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x, offset_y):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))
        
        if time.time() - self.last_score_update <= 5:
            win.blit(self.coin_image, (1230, 10))
        
            font = pygame.font.Font(None, 62)
            text = font.render(f"{self.score}", True, (BLACK))
            window.blit(text, (1180, 9))
         
        # Teken harten op basis van het aantal levens
        for i in range(self.lives):
            win.blit(self.heart_image, (10 + i * 45, 10))  # Positie aanpassen indien nodig

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name 
    
    def draw(self, win, offset_x, offset_y):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block2(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block3(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Small(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_block_small(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Block_Small2(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_block_small2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Block_Small3(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_block_small3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Bricks(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_bricks(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Bricks_Small(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_bricks_small(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Brown_Stone_Wide(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 3)
        block = get_brown_stone_wide(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Brown_Stone_Small(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size // 3)
        block = get_brown_stone_small(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Brown_Stone(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_brown_stone(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Brown_Stone_High(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size)
        block = get_brown_stone_high(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
 
class Brown_Stone_Jump(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 12 * 1.25)
        block = get_brown_stone_jump(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
               
class Stone_Wide(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 3)
        block = get_stone_wide(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Stone_Small(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size // 3)
        block = get_stone_small(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Stone(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_stone(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Stone_High(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size)
        block = get_stone_high(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Stone_Jump(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 12 * 1.25)
        block = get_stone_jump(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Stone_Hole(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_stone_hole(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Wood_Hole(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_wood_hole(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Leaves_Hole(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_leaves_hole(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Orange_Stone_Wide(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 3)
        block = get_orange_stone_wide(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Orange_Stone_Small(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size // 3)
        block = get_orange_stone_small(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Orange_Stone(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_orange_stone(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Orange_Stone_High(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size)
        block = get_orange_stone_high(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Gold_Wide(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 3)
        block = get_gold_wide(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Gold_Small(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size // 3)
        block = get_gold_small(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Gold(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3 * 2, size // 3 * 2)
        block = get_gold(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Gold_High(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size)
        block = get_gold_high(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Gold_Jump(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size // 12 * 1.25)
        block = get_gold_jump(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Dirt(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_dirt(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Dirt2(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_dirt2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Dirt3(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_dirt3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Fire(Object):
    ANIMATION_DELAY = 8

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Spikes(Object):

    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size // 6, "spikes")
        block = get_spikes(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Spikes_Down(Object):

    def __init__(self, x, y, size):
        super().__init__(x, y, size // 3, size // 6, "spikes_down")
        block = get_spikes_down(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
class Falling_Platform(Object):
    ANIMATION_DELAY = 3
    GRAVITY = 1

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "falling_platform")
        self.falling_platform = load_sprite_sheets("Traps", "Falling Platforms", width, height)
        self.image = self.falling_platform["on"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "on"
        self.y_vel = 0
        self.original_y = y
        self.fall_start_time = None  # Tijdstip waarop het vallen begint
        self.falling = False  # Of het platform al valt
        self.fall_count = 0  # Teller om de zwaartekracht op te bouwen
        self.rise_count = 0
        self.rising = False
        self.rise_start_time = None

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        
        # Kies de juiste sprite afhankelijk van de status
        if self.animation_name == "off":
            sprites = self.falling_platform["off"]
        else:
            sprites = self.falling_platform["on"]

        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def start_falling(self, current_time):
        """Start het vallen na 0 seconden."""
        if self.rising:
            self.fall_start_time = None
            self.falling = False
            return
        
        if not self.fall_start_time: # Stel de starttijd in als deze nog niet is ingesteld
            self.fall_start_time = current_time
                
        # Activeer het vallen na 0 seconden
        if current_time - self.fall_start_time >= 0:
            self.falling = True  # Zet de status op vallend
            
    def start_rising(self, current_time):
        """Start het vallen na 0 seconden."""
        if not self.rise_start_time: # Stel de starttijd in als deze nog niet is ingesteld
            self.rise_start_time = current_time
            
        # Activeer het vallen na 0 seconden
        if current_time - self.rise_start_time >= 5000:
            self.on()
            self.rising = True  # Zet de status op vallend
            self.rise_start_time = None
            
    def fall(self, fps, objects, player):
        """Laat het platform vallen."""
        if not self.falling or self.rise_count > 0:  # Controleer of het platform nog niet valt
            return

        # Bouw zwaartekracht op en beweeg het platform
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(0, self.y_vel)
        self.fall_count += 1  # Verhoog de val-teller
        
        # Hier kunnen we controleren of er een botsing plaatsvindt met andere objecten
        for other_obj in objects:
            # Controleer dat het andere object niet het platform zelf of de speler is
            if other_obj is self or other_obj is player or isinstance(other_obj, Coin):
                continue

            # Controleer of er een botsing is tussen dit platform en een ander object
            if pygame.sprite.collide_mask(self, other_obj):
                self.stop_fall()  # Stop het vallen van het platform
                self.rect.bottom = other_obj.rect.top
                self.start_rising(pygame.time.get_ticks())
                break
        
    def stop_fall(self):
        """Stop met vallen door de snelheid te resetten."""
        self.off()
        self.y_vel = 0
        self.fall_count = 0
        self.falling = False
        self.fall_start_time = None  # Reset de starttijd voor een volgende trigger
    
    def rise(self, fps, player):
        if not self.rising:  # Controleer of de stijgmodus actief is
            self.fall_start_time = None
            return
    
        if self.rect.y > self.original_y:  # Controleer of fall_count boven 0 is
            self.y_vel -= min(1, (self.rise_count / fps) * (self.GRAVITY/4))
            self.move(0, self.y_vel)
            self.rise_count += 1
            self.fall_start_time = None
        
        else:
            self.rect.y = self.original_y
            self.rise_count = 0
            self.rising = False
            self.y_vel = 0
            self.rise_start_time = None
            self.fall_start_time = None

class Fan(Object):
    ANIMATION_DELAY = 3
    GRAVITY = 0.2
    MAX_GRAVITY = 0.25
    SWITCH_INTERVAL = 5  # Interval om de fan aan/uit te schakelen (in seconden)

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fan")
        self.fan = load_sprite_sheets("Traps", "Fan", width, height)
        self.image = self.fan["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"
        self.fly_acceleration = 1
        self.is_on = False  # Fan start als uit
        self.last_switch_time = time.time()  # Houd bij wanneer de fan voor het laatst is geschakeld
        
    def switch_state(self):
        """Wissel de status van de fan (aan/uit)."""
        if self.is_on:
            self.off()
        else:
            self.on()

    def on(self):
        self.animation_name = "on"
        self.is_on = True

    def off(self):
        self.animation_name = "off"
        self.is_on = False

    def loop(self):
        current_time = time.time()
        if current_time - self.last_switch_time >= self.SWITCH_INTERVAL:
            self.switch_state()
            self.last_switch_time = current_time
            
        sprites = self.fan[self.animation_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        
    
    def affect_player(self, player, fps):
        """Voer effect op speler alleen uit als de fan aan staat."""
        if not self.is_on:
            player.is_gravity_active = True
            return  # Doe niets als de fan uit staat
        
        if not (self.rect.left <= player.rect.centerx and player.rect.centerx <= self.rect.right):
            self.fly_acceleration = 1
            return
        
        elif player.rect.bottom <= self.rect.top and (self.rect.top - player.rect.bottom) <= 200:
            # Bereken de oplopende negatieve y_vel
            player.is_gravity_active = False  # Zet zwaartekracht uit wanneer de fan de speler beïnvloedt
            self.fly_acceleration += self.GRAVITY  # Verhoog de valversnelling elke frame
            self.fly_acceleration = min(self.fly_acceleration, self.MAX_GRAVITY)  # Beperk de valversnelling
            player.y_vel -= self.fly_acceleration
        else:                
            # Als de speler verder dan 200 pixels boven de fan is, reset de fly_acceleration
            player.is_gravity_active = True
            self.fly_acceleration = 1  # Zet de versnelling terug naar het begin
            
class Twomp(Object):
    ANIMATION_DELAY = 12

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "twomp")
        self.twomp = load_sprite_sheets("Traps", "Rock Head", width, height)
        self.image = self.twomp["Blink (42x42)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Blink (42x42)"

    def blink(self):
        self.animation_name = "Blink (42x42)"

    def loop(self):
        sprites = self.twomp[self.animation_name]
        sprite_index = (self.animation_count // 
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Coin(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, 35, 35, "coin")
        coin = get_coin(size)
        self.image.blit(coin, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Finish_Cup(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, 46, 44, "finish_cup")
        finish_cup = get_finish_cup(size)
        self.image.blit(finish_cup, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x, offset_y):
    for tile in background:
        window.blit(bg_image, tile)
    
    for obj in objects:
        obj.draw(window, offset_x, offset_y)

    player.draw(window, offset_x, offset_y)

    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        # Skip collision for coins
        if isinstance(obj, (Coin, Finish_Cup)):
            collided_objects.append(obj)
            continue
        
        if pygame.sprite.collide_mask(player, obj):
            if isinstance(obj, (Stone_Jump, Brown_Stone_Jump, Gold_Jump)):
                # Als de speler naar beneden beweegt (landen)
                if dy > 0:
                    # De speler moet precies boven de stone_jump landen (niet erdoorheen vallen)
                    if player.rect.bottom >= obj.rect.top and player.rect.bottom + dy > obj.rect.top:
                        player.rect.bottom = obj.rect.top
                        player.landed()
                    else:  # Indien de speler zich niet correct bovenop de stone_jump bevindt
                        player.y_vel = 0  # Stop verticale snelheid
                        player.rect.bottom = obj.rect.top - 1  # Zet de speler net boven de steen om doorzakken te voorkomen
                        player.landed()  # Zorg ervoor dat de landingslogica ook hier gebeurt
                        
                elif dy < 0:  # Als de speler naar boven beweegt (springt)
                    # De speler mag niet door de stone_jump heen springen
                    if player.rect.top >= obj.rect.bottom and player.rect.top + dy < obj.rect.bottom:
                        player.rect.top = obj.rect.bottom
                        player.hit_head()
                        
            elif isinstance(obj, Falling_Platform) and obj.rising == True:
                continue

            else:
                # Voor andere objecten zoals platforms
                if isinstance(obj, Falling_Platform) and obj.falling:
                    continue
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()

            collided_objects.append(obj)
    
    return collided_objects
    
def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        # Skip collision for coins
        if isinstance(obj, (Coin, Finish_Cup)):
            continue
        
        if pygame.sprite.collide_mask(player, obj):
            if isinstance(obj, (Stone_Jump, Brown_Stone_Jump, Gold_Jump)):
                # Als de speler naar beneden komt (landt), mag hij niet door de stone_jump heen vallen
                if player.rect.bottom >= obj.rect.top or player.rect.bottom < obj.rect.top:
                    continue
            elif isinstance(obj, Falling_Platform) and obj.rising == True:
                continue
            else:
                collided_object = obj
                break

    player.move(-dx, 0)
    player.update()
    return collided_object

def handle_move(player, objects):
    keys = pygame.key.get_pressed()
    
    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2.6)
    collide_right = collide(player, objects, PLAYER_VEL * 2.6)

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not collide_left:
        player.move_left(PLAYER_VEL)
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]
    to_check_vertical = [*vertical_collide]

    for obj in to_check_vertical:
        if (obj and obj.name == "fire") or (obj and obj.name == "spikes") or (obj and obj.name == "spikes_down"):
            player.make_hit()
        
        if obj and isinstance(obj, Falling_Platform):
            if player.y_vel > 0:
                player.make_hit()  # Alleen als de speler echt van bovenaf raakt
            if player.y_vel <= 0: # Speler beweegt naar beneden en landt op het platform
                if obj.rect.y == obj.original_y:
                    obj.start_falling(pygame.time.get_ticks())  # Sla de tijd op wanneer de speler landt
                    
    for obj in to_check:        
        if obj and obj.name == "coin":
            # Controleer of de speler in aanraking komt met de coin
            if player.rect.colliderect(obj.rect):
                player.scores()
                print(f"Score: {player.score}")
                objects.remove(obj)  # Verwijder de coin uit de lijst, zodat deze niet opnieuw kan worden aangeraakt
                break  # We stoppen meteen met controleren van de andere coins zodra de speler een coin heeft geraakt
        
        elif obj and obj.name == "finish_cup":
            # Controleer of de speler in aanraking komt met de coin
            if player.rect.colliderect(obj.rect):
                global score
                score = player.score
                global level_completed
                level_completed = True
                objects.remove(obj)  # Verwijder de coin uit de lijst, zodat deze niet opnieuw kan worden aangeraakt
                break  # We stoppen meteen met controleren van de andere coins zodra de speler een coin heeft geraakt

# Functie voor het startscherm
def start_screen(window, self):
    # Haal de tegels en de achtergrondafbeelding op
    tiles, bg_image = get_background("Blue.png")  # Let op de juiste pad naar je afbeelding in de assets-map
    # Loop voor het startscherm
    while True:
        # Teken de achtergrond door de tiles te itereren
        for pos in tiles:
            window.blit(bg_image, pos)  # Plaats de afbeelding op elke positie in tiles

        # Bigbutton
        self.bigbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
        bigbutton_rect = pygame.Rect(170, 136, 1310, 835)  # Adjust the values as needed
        self.bigbutton_image = self.bigbutton_image.subsurface(bigbutton_rect)
        self.bigbutton_image = pygame.transform.scale(self.bigbutton_image, (WIDTH, HEIGHT,))  # Pas grootte aan indien nodig

        # Playbutton
        self.playbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
        playbutton_rect = pygame.Rect(128, 1144, 610, 250)  # Adjust the values as needed
        self.playbutton_image = self.playbutton_image.subsurface(playbutton_rect)
        self.playbutton_image = pygame.transform.scale(self.playbutton_image, (250, 60))  # Pas grootte aan indien nodig

        play_button = pygame.Rect((WIDTH // 2 - 125, HEIGHT // 2 - 50, 250, 60))  # Adjust position as needed

        # Quitbutton
        self.quitbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
        quitbutton_rect = pygame.Rect(128, 1790, 610, 250)  # Adjust the values as needed
        self.quitbutton_image = self.quitbutton_image.subsurface(quitbutton_rect)
        self.quitbutton_image = pygame.transform.scale(self.quitbutton_image, (250, 60))  # Pas grootte aan indien nodig

        quit_button = pygame.Rect((WIDTH // 2 - 125, HEIGHT // 2 + 50, 200, 50))  # Adjust position as needed

        window.blit(self.bigbutton_image, (0, 0, WIDTH, HEIGHT))
        window.blit(self.playbutton_image, (WIDTH // 2 - 125, HEIGHT // 2 - 50, 250, 60))
        window.blit(self.quitbutton_image, (WIDTH // 2 - 125, HEIGHT // 2 + 50, 250, 60))

        # Titel weergeven
        # Initialize font with bold attribute
        font = pygame.font.Font(None, 100)  # or load a specific font file like pygame.font.Font('your_font.ttf', 50)
        font.set_bold(True)  # Make the font bold

        title_text = font.render("Platformer", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        window.blit(title_text, title_rect)
        

        # Event handling voor knoppen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return  # Verlaat het startscherm om het spel te starten
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # Druk op 'F' om fullscreen in of uit te schakelen
                    toggle_fullscreen(window)

        pygame.display.flip()
        pygame.display.update(play_button)
        pygame.display.update(quit_button)

def draw_game_over_screen(window, self):
    font = pygame.font.Font(None, 80)
    font.set_bold(True)
    text = font.render("Game Over", True, (255, 0, 0))
    window.blit(text, (window.get_width() // 2 - text.get_width() // 2, window.get_height() // 3))

    # Teken de "Restart" knop
    restart_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2, 250, 60)
    
    # Playbutton
    self.restartbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    restart_rect = pygame.Rect(944, 1790, 610, 250)  # Adjust the values as needed
    self.restartbutton_image = self.restartbutton_image.subsurface(restart_rect)
    self.restartbutton_image = pygame.transform.scale(self.restartbutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.restartbutton_image, (WIDTH // 2 - 125, HEIGHT // 2, 250, 60))

    # Teken de "Exit" knop
    exit_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2 + 100, 250, 60)

    # Quitbutton
    self.exitbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    exitbutton_rect = pygame.Rect(944, 1144, 610, 250)  # Adjust the values as needed
    self.exitbutton_image = self.exitbutton_image.subsurface(exitbutton_rect)
    self.exitbutton_image = pygame.transform.scale(self.exitbutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.exitbutton_image, (WIDTH // 2 - 125, HEIGHT // 2 + 100, 250, 60))
      
    return restart_rect, exit_rect

def draw_escape_screen(window, self):
    
    # Teken de "Resume" knop
    resume_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2 - 105, 250, 60)
    
    # Resumebutton
    self.resumebutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    resume_rect = pygame.Rect(1740, 1790, 610, 250)  # Adjust the values as needed
    self.resumebutton_image = self.resumebutton_image.subsurface(resume_rect)
    self.resumebutton_image = pygame.transform.scale(self.resumebutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.resumebutton_image, (WIDTH // 2 - 125, HEIGHT // 2 - 105, 250, 60))
    
    # Teken de "Restart" knop
    restart_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2, 250, 60)
    
    # Restartbutton
    self.restartbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    restart_rect = pygame.Rect(944, 1790, 610, 250)  # Adjust the values as needed
    self.restartbutton_image = self.restartbutton_image.subsurface(restart_rect)
    self.restartbutton_image = pygame.transform.scale(self.restartbutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.restartbutton_image, (WIDTH // 2 - 125, HEIGHT // 2, 250, 60))

    # Teken de "Exit" knop
    exit_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2 + 105, 250, 60)

    # Exitbutton
    self.exitbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    exitbutton_rect = pygame.Rect(944, 1144, 610, 250)  # Adjust the values as needed
    self.exitbutton_image = self.exitbutton_image.subsurface(exitbutton_rect)
    self.exitbutton_image = pygame.transform.scale(self.exitbutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.exitbutton_image, (WIDTH // 2 - 125, HEIGHT // 2 + 105, 250, 60))
        
    return resume_rect, restart_rect, exit_rect

def draw_level_completed_screen(window, self):
    font = pygame.font.Font(None, 80)
    font.set_bold(True)
    text = font.render("Level Completed", True, (0, 0, 0))
    window.blit(text, (window.get_width() // 2 - text.get_width() // 2, window.get_height() // 3 - 64))
    
    self.coin_image = pygame.image.load(join("assets", "Items","Coin", "coin.png")).convert_alpha()
    self.coin_image = pygame.transform.scale(self.coin_image, (35, 35))  # Pas grootte aan indien nodig
    window.blit(self.coin_image, ((window.get_width() // 2) + 70, window.get_height() // 3 + 20))
        
    font2 = pygame.font.Font(None, 62)
    text2 = font2.render(f"Score: {score}", True, (BLACK))
    window.blit(text2, ((window.get_width() // 2) - 120, window.get_height() // 3 + 19))

    # Teken de "Restart" knop
    restart_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2, 250, 60)
    
    # Playbutton
    self.restartbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    restart_rect = pygame.Rect(944, 1790, 610, 250)  # Adjust the values as needed
    self.restartbutton_image = self.restartbutton_image.subsurface(restart_rect)
    self.restartbutton_image = pygame.transform.scale(self.restartbutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.restartbutton_image, (WIDTH // 2 - 125, HEIGHT // 2, 250, 60))

    # Teken de "Exit" knop
    exit_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2 + 100, 250, 60)

    # Quitbutton
    self.exitbutton_image = pygame.image.load(join("assets", "Menu", "Buttons", "buttons.png")).convert_alpha()
    exitbutton_rect = pygame.Rect(944, 1144, 610, 250)  # Adjust the values as needed
    self.exitbutton_image = self.exitbutton_image.subsurface(exitbutton_rect)
    self.exitbutton_image = pygame.transform.scale(self.exitbutton_image, (250, 60))  # Pas grootte aan indien nodig

    window.blit(self.exitbutton_image, (WIDTH // 2 - 125, HEIGHT // 2 + 100, 250, 60))
      
    return restart_rect, exit_rect

class Game:
    def __init__(self):
        self.fullscreen = False  # Variabele om fullscreen status op te slaan
        self.game_paused = False  # To keep track of whether the game is paused
    
    def initialize_game(self):
        
        self.clock = pygame.time.Clock()
        self.background, self.bg_image = get_background("Brown.png")

        block_size = 96
        self.player = Player(100, 700, 50, 50)

        fire = Fire(block_size * 5, HEIGHT - (block_size * 3) - 64, 16, 32)
        fire2 = Fire(block_size * 5.5, HEIGHT - (block_size * 3) - 64, 16, 32)
        fire3 = Fire(block_size * 6, HEIGHT - (block_size * 3) - 64, 16, 32)
        fire4 = Fire(block_size * 6.5, HEIGHT - (block_size * 3) - 64, 16, 32)
        self.fires = [fire, fire2, fire3, fire4]
        [fire.on() for fire in self.fires]
        
        spikes = Spikes(block_size * 48, HEIGHT - block_size * 11 - 16, block_size)
        spikes2 = Spikes(block_size * 48 + 32, HEIGHT - block_size * 11 - 16, block_size)
        self.spikes = [spikes, spikes2]
        
        falling_platform = Falling_Platform(block_size * 2 + 16, HEIGHT - block_size * 5, 32, 10)
        falling_platform2 = Falling_Platform(block_size * 13 + 16, HEIGHT - block_size * 8, 32, 10)
        falling_platform3 = Falling_Platform(block_size * 15 + 16, HEIGHT - block_size * 10, 32, 10)
        falling_platform4 = Falling_Platform(block_size * 17 + 16, HEIGHT - block_size * 11, 32, 10)
        falling_platform5 = Falling_Platform(block_size * 16 + 16, HEIGHT - block_size * 12, 32, 10)
        self.falling_platforms = [falling_platform, falling_platform2, falling_platform3, falling_platform4, falling_platform5]
        [falling_platform.on() for falling_platform in self.falling_platforms]
        
        fan = Fan(block_size * 12 + 24, HEIGHT - (block_size * 1) - 16, 24, 8)
        fan2 = Fan(block_size * 41 + 24, HEIGHT - (block_size * 8) - 16, 24, 8)
        fan3 = Fan(block_size * 43, HEIGHT - block_size * 13, 24, 8)
        fan4 = Fan(block_size * 49, HEIGHT - block_size * 11, 24, 8)
        self.fans = [fan, fan2, fan3, fan4]
        [fan.on() for fan in self.fans]
        
        coin = Coin((block_size * 2) + 31.5, (HEIGHT - block_size * 9) + 57, block_size)
        coin2 = Coin((block_size * 2) + 31.5, (HEIGHT - block_size * 3) + 57, block_size)
        coin3 = Coin((block_size * 8) + 31.5, (HEIGHT - block_size * 6) + 57, block_size)
        coin4 = Coin((block_size * 9) + 31.5, (HEIGHT - block_size * 9) + 57, block_size)
        coin5 = Coin((block_size * 14) + 45, (HEIGHT - block_size * 13) + 57, block_size)
        coin6 = Coin((block_size * 15) + 15, (HEIGHT - block_size * 13) + 57, block_size)
        coin7 = Coin((block_size * 31) + 40, (HEIGHT - block_size * 11) + 47, block_size)
        coin8 = Coin((block_size * 31.5) + 40, (HEIGHT - block_size * 11) + 47, block_size)
        coin9 = Coin((block_size * 32) + 40, (HEIGHT - block_size * 11) + 47, block_size)
        coin10 = Coin((block_size * 32.5) + 40, (HEIGHT - block_size * 11) + 47, block_size)
        coin11 = Coin((block_size * 48.5) + 16, (HEIGHT - block_size * 12) + 47, block_size)
        coin12 = Coin((block_size * 51) + 40, (HEIGHT - block_size * 17) + 47, block_size)
        self.coins = [coin, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12]
        
        brown_stone_wide = Brown_Stone_Wide(block_size * 14, HEIGHT - block_size * 12, block_size)
        brown_stone_wide2 = Brown_Stone_Wide(block_size * 15, HEIGHT - block_size * 12, block_size)
        brown_stone_wide3 = Brown_Stone_Wide(block_size * 18, HEIGHT - block_size * 9, block_size)
        brown_stone_wide4 = Brown_Stone_Wide(block_size * 28, HEIGHT - block_size * 11, block_size)
        self.brown_stone_wides = [brown_stone_wide, brown_stone_wide2, brown_stone_wide3, brown_stone_wide4]
        
        brown_stone_small = Brown_Stone_Small(block_size * 21, HEIGHT - block_size * 10, block_size)
        brown_stone_small2 = Brown_Stone_Small(block_size * 25, HEIGHT - block_size * 10, block_size)
        brown_stone_small3 = Brown_Stone_Small(block_size * 31 + 32, HEIGHT - block_size * 9, block_size)
        brown_stone_small4 = Brown_Stone_Small(block_size * 37.5, HEIGHT - block_size * 11, block_size)
        self.brown_stone_smalls = [brown_stone_small, brown_stone_small2, brown_stone_small3, brown_stone_small4]
        
        brown_stone_jump = Brown_Stone_Jump(block_size * 31 + 32, HEIGHT - block_size * 10 - 10, block_size)
        brown_stone_jump2 = Brown_Stone_Jump(block_size * 32 + 32, HEIGHT - block_size * 10 - 10, block_size)
        brown_stone_jump3 = Brown_Stone_Jump(block_size * 31 + 32, HEIGHT - block_size * 12, block_size)
        brown_stone_jump4 = Brown_Stone_Jump(block_size * 32 + 32, HEIGHT - block_size * 12, block_size)
        self.brown_stone_jumps = [brown_stone_jump, brown_stone_jump2, brown_stone_jump3, brown_stone_jump4]
        
        brown_stone_high = Brown_Stone_High(block_size * 14, HEIGHT - block_size * 13, block_size)
        brown_stone_high2 = Brown_Stone_High(block_size * 15 + 64, HEIGHT - block_size * 13, block_size)
        brown_stone_high3 = Brown_Stone_High(block_size * 14, HEIGHT - block_size * 14, block_size)
        brown_stone_high4 = Brown_Stone_High(block_size * 15 + 64, HEIGHT - block_size * 14, block_size)
        brown_stone_high5 = Brown_Stone_High(block_size * 18, HEIGHT - block_size * 11, block_size)
        brown_stone_high6 = Brown_Stone_High(block_size * 18, HEIGHT - block_size * 12, block_size)
        brown_stone_high7 = Brown_Stone_High(block_size * 18, HEIGHT - block_size * 13, block_size)
        brown_stone_high8 = Brown_Stone_High(block_size * 18, HEIGHT - block_size * 14, block_size)
        brown_stone_high9 = Brown_Stone_High(block_size * 31, HEIGHT - block_size * 11, block_size)
        brown_stone_high10 = Brown_Stone_High(block_size * 31, HEIGHT - block_size * 12, block_size)
        brown_stone_high11 = Brown_Stone_High(block_size * 33 + 32, HEIGHT - block_size * 11, block_size)
        brown_stone_high12 = Brown_Stone_High(block_size * 33 + 32, HEIGHT - block_size * 12, block_size)
        self.brown_stone_highs = [brown_stone_high, brown_stone_high2, brown_stone_high3, brown_stone_high4, brown_stone_high5, 
                                  brown_stone_high6, brown_stone_high7, brown_stone_high8, brown_stone_high9, brown_stone_high10, brown_stone_high11, brown_stone_high12]
        
        stone_wide = Stone_Wide(block_size * 42, HEIGHT - block_size * 13, block_size)
        stone_wide2 = Stone_Wide(block_size * 48, HEIGHT - block_size * 11, block_size)
        stone_wide3 = Stone_Wide(block_size * 47, HEIGHT - block_size * 16, block_size)
        stone_wide4 = Stone_Wide(block_size * 48, HEIGHT - block_size * 16, block_size)
        stone_wide5 = Stone_Wide(block_size * 49, HEIGHT - block_size * 16, block_size)
        stone_wide6 = Stone_Wide(block_size * 51, HEIGHT - block_size * 16, block_size)
        self.stone_wides = [stone_wide, stone_wide2, stone_wide3, stone_wide4, stone_wide5, stone_wide6]
        
        stone_small = Stone_Small(block_size * 43, HEIGHT - block_size * 13 + 16, block_size)
        stone_small2 = Stone_Small(block_size * 49, HEIGHT - block_size * 11 + 16, block_size)
        self.stone_smalls = [stone_small, stone_small2]
        
        stone_high = Stone_High(block_size * 47, HEIGHT - block_size * 17, block_size)
        stone_high2 = Stone_High(block_size * 47, HEIGHT - block_size * 18, block_size)
        stone_high3 = Stone_High(block_size * 47, HEIGHT - block_size * 19, block_size)
        self.stone_highs = [stone_high, stone_high2, stone_high3]
        
        stone_jump = Stone_Jump(block_size * 50, HEIGHT - block_size * 16, block_size)
        self.stone_jumps = [stone_jump]
        
        finish_cup = Finish_Cup(block_size * 48 + 25, HEIGHT - block_size * 17 + 52, block_size)
        self.finish_cups = [finish_cup]

        dirt1 = Dirt(block_size * -2, HEIGHT - block_size * 1, block_size)
        dirt2 = Dirt(block_size * -2, HEIGHT - block_size * 2, block_size)
        dirt3 = Dirt(block_size * -2, HEIGHT - block_size * 3, block_size)
        dirt4 = Dirt(block_size * -2, HEIGHT - block_size * 4, block_size)
        dirt5 = Dirt(block_size * -2, HEIGHT - block_size * 5, block_size)
        dirt6 = Dirt(block_size * -2, HEIGHT - block_size * 6, block_size)
        dirt7 = Dirt(block_size * -2, HEIGHT - block_size * 7, block_size)
        dirt8 = Dirt(block_size * -2, HEIGHT - block_size * 8, block_size)
        dirt9 = Dirt(block_size * -2, HEIGHT - block_size * 9, block_size)
        dirt10 = Dirt(block_size * -2, HEIGHT - block_size * 10, block_size)
        dirt11 = Dirt(block_size * 2, HEIGHT - block_size * 1, block_size)
        block1 = Block(block_size * 2, HEIGHT - block_size * 2, block_size)
        block2 = Block(block_size * 4, HEIGHT - block_size * 3, block_size)
        block3 = Block(block_size * 5, HEIGHT - block_size * 3, block_size)
        block4 = Block(block_size * 6, HEIGHT - block_size * 3, block_size)
        dirt12 = Dirt(block_size * 7, HEIGHT - block_size * 3, block_size)
        dirt13 = Dirt(block_size * 7, HEIGHT - block_size * 4, block_size)
        block5 = Block(block_size * 7, HEIGHT - block_size * 5, block_size)
        block6 = Block(block_size * 8, HEIGHT - block_size * 5, block_size)
        block7 = Block(block_size * 9, HEIGHT - block_size * 8, block_size)
        block8 = Block(block_size * 10, HEIGHT - block_size * 8, block_size)
        block9 = Block(block_size * 11, HEIGHT - block_size * 6, block_size)
        dirt14 = Dirt(block_size * 11, HEIGHT - block_size * 5, block_size)
        dirt15 = Dirt(block_size * 11, HEIGHT - block_size * 4, block_size)
        dirt16 = Dirt(block_size * 11, HEIGHT - block_size * 3, block_size)
        dirt17 = Dirt(block_size * 11, HEIGHT - block_size * 2, block_size)
        dirt18 = Dirt(block_size * 11, HEIGHT - block_size * 1, block_size)
        dirt2_1 = Dirt2(block_size * 40, HEIGHT - block_size * 8, block_size)
        dirt2_2 = Dirt2(block_size * 40, HEIGHT - block_size * 9, block_size)
        dirt2_3 = Dirt2(block_size * 40, HEIGHT - block_size * 10, block_size)
        dirt2_4 = Dirt2(block_size * 54, HEIGHT - block_size * 8, block_size)
        dirt2_5 = Dirt2(block_size * 54, HEIGHT - block_size * 9, block_size)
        dirt2_6 = Dirt2(block_size * 54, HEIGHT - block_size * 10, block_size)
        dirt2_7 = Dirt2(block_size * 54, HEIGHT - block_size * 11, block_size)
        dirt2_8 = Dirt2(block_size * 54, HEIGHT - block_size * 12, block_size)
        dirt2_9 = Dirt2(block_size * 54, HEIGHT - block_size * 13, block_size)
        dirt2_10 = Dirt2(block_size * 54, HEIGHT - block_size * 14, block_size)
        dirt2_11 = Dirt2(block_size * 54, HEIGHT - block_size * 15, block_size)
        dirt2_12 = Dirt2(block_size * 54, HEIGHT - block_size * 16, block_size)
        dirt2_13 = Dirt2(block_size * 54, HEIGHT - block_size * 17, block_size)
        dirt2_14 = Dirt2(block_size * 54, HEIGHT - block_size * 18, block_size)
        dirt2_15 = Dirt2(block_size * 54, HEIGHT - block_size * 19, block_size)
        dirt2_16 = Dirt2(block_size * 54, HEIGHT - block_size * 20, block_size)
        dirt2_17 = Dirt2(block_size * 54, HEIGHT - block_size * 21, block_size)
        block2_1 = Block2(block_size * 40, HEIGHT - block_size * 11, block_size)
        
        self.blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9]
        self.dirts = [dirt1, dirt2, dirt3, dirt4, dirt5, dirt6, dirt7, dirt8, dirt9, dirt10, dirt11,
                      dirt12, dirt13, dirt14, dirt15, dirt16, dirt17, dirt18]
        self.blocks2 = [block2_1]
        self.dirts2 = [dirt2_1, dirt2_2, dirt2_3, dirt2_4, dirt2_5, dirt2_6, dirt2_7, dirt2_8, dirt2_9, dirt2_10,
                       dirt2_11, dirt2_12, dirt2_13, dirt2_14, dirt2_15, dirt2_16, dirt2_17]
        
        self.test = []

        self.low_floor = [Block(i * block_size, HEIGHT - block_size, block_size) 
                 for i in range(-2,18)] + [Dirt(i * block_size, HEIGHT, block_size)
               for i in range(-2,18)]
        
        self.high_floor = [Block(i * block_size, HEIGHT - block_size * 8, block_size) 
                 for i in range(18, 40)] + [Dirt(i * block_size, HEIGHT - block_size * a, block_size)
               for i in range(18, 40) for a in range(0,8)] + [Spikes(i * block_size, HEIGHT - block_size * 8 - 16, block_size) 
                 for i in range(18, 40)] + [Spikes(i * block_size + 32, HEIGHT - block_size * 8 - 16, block_size) 
                 for i in range(18, 40)] + [Spikes(i * block_size + 64, HEIGHT - block_size * 8 - 16, block_size) 
                 for i in range(18, 40)]

        self.high_floor2 = [Block2(i * block_size, HEIGHT - block_size * 8, block_size) 
                 for i in range(40, 55)] + [Dirt2(i * block_size, HEIGHT - block_size * a, block_size)
               for i in range(40, 55) for a in range(0,8)]
        
        self.floor = self.low_floor + self.high_floor + self.high_floor2

        self.objects = [*self.floor, *self.blocks, *self.dirts, *self.blocks2, *self.dirts2, *self.fires, *self.brown_stone_jumps, 
                        *self.brown_stone_wides, *self.brown_stone_highs, *self.brown_stone_smalls, *self.stone_wides, *self.stone_smalls, *self.stone_highs, 
                        *self.stone_jumps, *self.coins, *self.finish_cups, *self.spikes, *self.falling_platforms, *self.test, *self.fans]

        self.offset_x = 0
        self.offset_y = 0
        self.scroll_area_width = 400
        self.scroll_area_height_top = 200

        global game_over
        game_over = False
        
        global level_completed
        level_completed = False

        self.run = True
    
    def toggle_fullscreen(self, window):
        if self.fullscreen:
            pygame.display.set_mode((WIDTH, HEIGHT))
        else:
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    
        self.fullscreen = not self.fullscreen  # Wissel status om 

    def start_game(self):
        start_screen(window, self)
        self.initialize_game()
        while self.run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break

                if event.type == pygame.KEYDOWN and not self.game_paused:
                    if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                        self.player.jump()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_paused = True  # Zet de game in pauze
                    
                # Toggle fullscreen met F11 (of een andere toets naar keuze)
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:  # Druk op 'F' om fullscreen in of uit te schakelen
                            toggle_fullscreen(window)
                            
            if game_over:
            # Draw the game over screen and buttons
                restart_rect, exit_rect = draw_game_over_screen(window, self)  # Teken het game over-scherm en de knoppen
                restart_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2, 250, 60)
                pygame.display.update()
                self.game_paused = True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rect.collidepoint(event.pos):
                            # Start de game opnieuw
                            self.initialize_game()
                            self.game_paused = False  # Hervat de game
                            # Zet hier ook andere variabelen terug naar de startwaarden als nodig
                        elif exit_rect.collidepoint(event.pos):
                            self.game_paused = False  # Hervat de game
                            return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:  # Druk op 'F' om fullscreen in of uit te schakelen
                            toggle_fullscreen(window)
                            # Ga terug naar het beginscherm of sluit de game
                continue  # Sla de rest van de loop over
            
            if level_completed:
            # Draw the game over screen and buttons
                restart_rect, exit_rect = draw_level_completed_screen(window, self)  # Teken het game over-scherm en de knoppen
                restart_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2, 250, 60)
                pygame.display.update()
                self.game_paused = True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rect.collidepoint(event.pos):
                            # Start de game opnieuw
                            self.initialize_game()
                            self.game_paused = False  # Hervat de game
                            # Zet hier ook andere variabelen terug naar de startwaarden als nodig
                        elif exit_rect.collidepoint(event.pos):
                            self.game_paused = False  # Hervat de game
                            return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:  # Druk op 'F' om fullscreen in of uit te schakelen
                            toggle_fullscreen(window)
                            # Ga terug naar het beginscherm of sluit de game
                continue  # Sla de rest van de loop over

            if self.game_paused:
                resume_rect, restart_rect, exit_rect = draw_escape_screen(window, self)  # Teken het escape-scherm en de knoppen
                resume_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2 - 105, 250, 60)
                restart_rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2, 250, 60)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if resume_rect.collidepoint(event.pos):
                            self.game_paused = False  # Hervat de game
                        elif restart_rect.collidepoint(event.pos):
                            self.game_paused = False
                            self.initialize_game()
                        elif exit_rect.collidepoint(event.pos):
                            self.game_paused = False  # Hervat de game
                            return  # Verlaat de game en ga terug naar het startscherm
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.game_paused = False  # Hervat de game
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:  # Druk op 'F' om fullscreen in of uit te schakelen
                            toggle_fullscreen(window)
                        # Ga terug naar het beginscherm of sluit de game
                continue  # Ga verder met de volgende iteratie

            self.player.loop(FPS) 
            [fire.loop() for fire in self.fires]
            [fan.loop() for fan in self.fans]
            
            #for falling_platform in self.falling_platforms:
                #if falling_platform.rising or falling_platform.falling:
                 #   falling_platform.on()
                #elif falling_platform.rise_start_time and pygame.time.get_ticks() - falling_platform.rise_start_time < 5000:
                   # falling_platform.off()
                #else:
                  #  falling_platform.on()
                
            [falling_platform.loop() for falling_platform in self.falling_platforms]   
            handle_move(self.player, self.objects)
            
            if not game_over or not level_completed:
                draw(window, self.background, self.bg_image, self.player, self.objects, self.offset_x, self.offset_y)

            if((self.player.rect.right - self.offset_x >= WIDTH - self.scroll_area_width) and self.player.x_vel > 0) or (
                    (self.player.rect.left - self.offset_x <= self.scroll_area_width) and self.player.x_vel < 0):
                self.offset_x += self.player.x_vel

            # Stel de scroll_area_height in op 400 als self.player.rect.bottom lager is dan -100
            if self.player.rect.bottom <= 408:
                self.scroll_area_height_bottom = 450
            else:
                self.scroll_area_height_bottom = 148

            # Normale scroll logica met de aangepaste scroll_area_height
            if ((self.player.rect.top - self.offset_y >= HEIGHT - self.scroll_area_height_bottom) and self.player.y_vel > 0) or (
                    (self.player.rect.bottom - self.offset_y <= self.scroll_area_height_top) and self.player.y_vel < 0):
                self.offset_y += self.player.y_vel 
                
            for obj in self.objects:
                if isinstance(obj, Falling_Platform):
                    obj.fall(FPS, self.objects, self.player)  # Blijf de fall-functie aanroepen zolang het platform valt
                    obj.rise(FPS, self.player)
                    
                    if obj.rise_start_time != None:
                        obj.start_rising(pygame.time.get_ticks())

                if isinstance(obj, Fan):
                    obj.affect_player(self.player, FPS)
                    

def main(window):
    game = Game()
    
    while True:
        game.start_game()

        if not game.run:
            break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)