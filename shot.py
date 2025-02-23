import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt



