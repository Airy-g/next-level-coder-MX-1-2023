import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obtacles = []

    def update(self, game_speed, game):

        if len(self.obtacles) == 0:
            self.obtacles.append(Cactus(SMALL_CACTUS))

        for obtacle in self.obtacles:
            obtacle.update(game_speed, self.obtacles)
            
            if game.player.dino_rect.colliderect(obtacle.rect):
                pygame.time.delay(300)
                game.playing = False
                break

    def draw(self, screen):
        for obstacles in self.obtacles:
            obstacles.draw(screen)