import sys
import pygame
from constants import *
from player import Player, Shot
from Asteroid import Asteroid
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")

    shots = pygame.sprite.Group() #the variable that stores shot data
     # groups for the sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # This is the loop that keeps the game running
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                new_shot = player.shoot()
                if new_shot:
                    shots.add(new_shot)
        screen.fill((0, 0, 0))
        for sprite in updatable:
            sprite.update(dt)
            
        for shot in shots:
            for asteroid in asteroids:
               if pygame.sprite.collide_rect(shot, asteroid):
                   shot.kill()
                   asteroid.split()


        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game Over")
                sys.exit()
        
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        
        

        dt = clock.tick(60) / 1000

        

        # The following code will tell us the fps
        #fps = clock.get_fps()
        #print (f"current FPS: {fps}")



if __name__ == "__main__":
    main()
