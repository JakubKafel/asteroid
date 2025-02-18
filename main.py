# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    #group creation
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    player_start_x = SCREEN_WIDTH/2
    player_start_y = SCREEN_HEIGHT/2

    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids,updatables,drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots,drawables,updatables)

    asteroidfield = AsteroidField()

    player = Player(player_start_x, player_start_y)
    
#main game loop
    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        #drawing groups
        updatables.update(dt)

        for obj in drawables:
            obj.draw(screen)
       

        pygame.display.flip()

        #collision check
        for obj in asteroids:
            for shot in shots:
                if obj.detectcollision(shot):
                    obj.split()
                    shot.kill()

            if player.detectcollision(obj):
                print("Game over!")
                return

        
        
    #FPS limit = 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()