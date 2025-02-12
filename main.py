# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    player_start_x = SCREEN_WIDTH/2
    player_start_y = SCREEN_HEIGHT/2
    player = Player(player_start_x, player_start_y)

#main game loop
    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        #drawing player
        player.update(dt)
        player.draw(screen)



        pygame.display.flip()

    #FPS limit = 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()