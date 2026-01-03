import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return          
        
        log_state()
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip() 
        dt = clock.tick(60) / 1000
  




if __name__ == "__main__":
    main()
