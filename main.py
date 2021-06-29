# Imports
import pygame
import os
import time
import random

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
    Y_POS = 300
    Y_DUCK_POS = 270
    JUMP_HEIGHT = 100

    def __init__(self):
        self.run_img = DINO_RUN_IMGS
        self.jump_img = DINO_JUMP_IMGS
        self.duck_img = DINO_DUCK_IMGS

        self.img = self.run_img[0]

        self.rect = self.img.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.animate_tick = 0

        self.run = True
        self.jump = False
        self.duck = False

    def update(self):
        if self.animate_tick >= 9:
            self.animate_tick = 0

        if self.run:
            self.run()

        if self.jump:
            self.jump()

        if self.duck:
            self.duck()

        self.animate_tick += 1

    def run(self):
        self.run = True
        self.jump = False
        self.duck = False

        if self.animate_tick // 5 == 1:
            self.img = self.run_img[1]
        else:
            self.img = self.run_img[0]

    def jump(self):
        self.jump = True
        self.duck = False
        self.run = False

        if self.animate_tick // 5 == 1:
            self.img = self.jump_img[1]
        else:
            self.img = self.jump_img[0]

    def duck(self):
        self.duck = True
        self.jump = False
        self.run = True

        if self.animate_tick // 5 == 1:
            self.img = self.duck_img[1]
        else:
            self.img = self.duck_img[0]

    def draw(self, WIN):
        WIN.blit(self.img, (self.rect.x, self.rect.y))


# Main
def main():
    clock = pygame.time.Clock()
    game_speed = 14 
    game = True

    dino = Dino()

    while game:
        WIN.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        dino.update()
        dino.draw(WIN)

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()