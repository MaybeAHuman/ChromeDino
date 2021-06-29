# Imports
import pygame
import os
import time
import random

from pygame.constants import K_DOWN, K_UP

# Create Canvas 
WIN_WIDTH = 1000
WIN_HEIGHT = 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Dino")


# Assets
DINO_RUN_IMGS = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")), 
                 pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

DINO_JUMP_IMGS = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")), 
                  pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

DINO_DUCK_IMGS = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")), 
                  pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

CACTUS_IMGS = [pygame.image.load(os.path.join("Assets/Cactus", file)) for file in os.listdir("Assets/Cactus")]

BIRD_IMGS = [pygame.image.load(os.path.join("Assets/Bird", file)) for file in os.listdir("Assets/Bird")]

TRACK_IMG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
CLOUD_IMG = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
RESET_IMG = pygame.image.load(os.path.join("Assets/Other", "Reset.png"))
GAMEOVER_IMG = pygame.image.load(os.path.join("Assets/Other", "GameOver.png"))

# Dino
class Dino():
    X_POS = 75
    Y_POS = 280
    Y_DUCK_POS = 304.5
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = DINO_RUN_IMGS
        self.jump_img = DINO_JUMP_IMGS
        self.duck_img = DINO_DUCK_IMGS

        self.img = self.run_img[0]

        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.animate_tick = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.jump_vel = self.JUMP_VEL

    def update(self, userInput):
        if self.animate_tick >= 9:
            self.animate_tick = 0
        
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()

        if userInput[K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif userInput[K_DOWN] and not self.dino_duck:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def run(self):
        self.img = self.run_img[self.animate_tick // 5]
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.animate_tick += 1

    def duck(self):
        self.img = self.duck_img[self.animate_tick // 5]
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_DUCK_POS
        self.animate_tick += 1
    
    def jump(self):
        self.dino_jump = self.jump_img[self.animate_tick // 5]
        self.animate_tick += 1

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 3.2
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.jump_vel = self.JUMP_VEL
            self.dino_jump = False
            
    def draw(self, WIN):
        WIN.blit(self.img, (self.dino_rect.x, self.dino_rect.y))

# Background
class Background():
    TRACK_IMG = TRACK_IMG
    CLOUD_IMG = CLOUD_IMG
    TRACK_WIDTH = TRACK_IMG.get_width()
    CLOUD_WIDTH = CLOUD_IMG.get_width()
    GAME_VEL = 14
    SCREEN_WIDTH = WIN_WIDTH


    def __init__(self):
        self.track_x1 = 0
        self.track_x2 = self.TRACK_WIDTH
        self.track_y = 294

        self.cloud_x1 = self.SCREEN_WIDTH + random.randint(500, 800)
        self.cloud_x2 = self.cloud_x1 + random.randint(300, 500)
        self.cloud_x3 = self.cloud_x2 + random.randint(300, 500)
        self.cloud_y = random.randint(25, 100)

    def move(self):
        self.track_x1 -= self.GAME_VEL
        self.track_x2 -= self.GAME_VEL

        self.cloud_x1 -= self.GAME_VEL
        self.cloud_x2 -= self.GAME_VEL
        self.cloud_x3 -= self.GAME_VEL

        if self.track_x1 < -self.TRACK_WIDTH:
            self.track_x1 = self.track_x2 + self.TRACK_WIDTH

        if self.track_x2 < -self.TRACK_WIDTH:
            self.track_x2 = self.track_x1 + self.TRACK_WIDTH

        if self.cloud_x1 < -self.CLOUD_WIDTH:
            self.cloud_x1 = self.SCREEN_WIDTH + random.randint(500, 800)
        if self.cloud_x2 < -self.CLOUD_WIDTH:
            self.cloud_x2 = self.cloud_x1 + random.randint(300, 500)
        if self.cloud_x2 < -self.CLOUD_WIDTH:
            self.cloud_x3 = self.cloud_x2 + random.randint(300, 500)

    def draw(self, WIN):
        WIN.blit(self.TRACK_IMG, (self.track_x1, self.track_y))
        WIN.blit(self.TRACK_IMG, (self.track_x2, self.track_y))

        WIN.blit(self.CLOUD_IMG, (self.cloud_x1, self.cloud_y))
        WIN.blit(self.CLOUD_IMG, (self.cloud_x2, self.cloud_y))
        WIN.blit(self.CLOUD_IMG, (self.cloud_x3, self.cloud_y))

# Main
def main():
    clock = pygame.time.Clock()
    game = True

    dino = Dino()

    bg = Background()

    while game:
        WIN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        dino.update(userInput)
        dino.draw(WIN)

        bg.move()
        bg.draw(WIN)

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()
