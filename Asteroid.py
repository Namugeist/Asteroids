import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius) 
        self.velocity = velocity 

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA) 
        self.rect = self.image. get_rect()
        self.rect.center = (x,y)


    def draw(self, screen):
        pygame.draw.circle(screen, "Green", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt
       self.rect.center = (self.position.x, self.position.y)
    
    def split (self):

            #print("Original radius:", self.radius)
           # print("ASTEROID_MIN_RADIUS:", ASTEROID_MIN_RADIUS)
           # print("New radius:", self.radius - ASTEROID_MIN_RADIUS)
    # ... rest of your code
            self.kill()
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            random_angle = random.uniform (20, 50)

            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x, y = self.rect.center
            Asteroid(x, y, new_radius, velocity1 * 1.2)
            Asteroid(x, y ,new_radius, velocity2 *1.2)
