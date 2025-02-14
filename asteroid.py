import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x,y,radius)



    def draw(self,screen: pygame.display) -> None:
        pygame.draw.circle(screen,'white',self.position,self.radius,2)
    
    def update(self,dt: float) -> None:
        self.position += self.velocity * dt