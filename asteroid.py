import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x,y,radius)



    def draw(self,screen: pygame.display) -> None:
        pygame.draw.circle(screen,'white',self.position,self.radius,2)
    
    def update(self,dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            new_vector_1 = self.velocity.rotate(random_angle)
            new_vector_2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_aseroid_1 = Asteroid(self.position[0],self.position[1],new_radius)
            new_aseroid_2 = Asteroid(self.position[0],self.position[1],new_radius)

            new_aseroid_1.velocity = new_vector_1 * 1.2
            new_aseroid_2.velocity = new_vector_2 * 1.2