import pygame
from constants import *
from circleshape import CircleShape
class Player (CircleShape):
    
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate (self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        self.cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move (self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown_timer <= 0:
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN
            direction = pygame.Vector2(0,1)
            direction= direction.rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            return Shot (self.position.x, self.position.y, velocity)
        return None
        
     
        



        
class Shot (CircleShape):
    def __init__(self, x, y,velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2 ), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self, dt):
       self.position += self.velocity * dt
       self.rect.center = self.position

    def draw(self,screen):
        pygame.draw.circle(screen,(255,0,255), self.position, SHOT_RADIUS)
    
       