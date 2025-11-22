import pygame
import circleshape

from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, 5)
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt