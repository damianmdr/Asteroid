import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return          
        
        log_state()
        screen.fill("black")
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip() 
        dt = clock.tick(60) / 1000
  




if __name__ == "__main__":
    main()
