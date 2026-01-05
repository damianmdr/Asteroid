import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from logger import log_event
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            a = random.uniform(20,50)
            b = self.velocity.rotate(a) * 1.2
            c = self.velocity.rotate(-a) * 1.2
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid1.velocity = b

            asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)  
            asteroid2.velocity = c   
     
            




