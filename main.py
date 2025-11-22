import pygame
import player
import asteroid
import asteroidfield
import sys
import shot

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)
    ship = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = asteroidfield.AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            if ship.collides_with(ast):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for sh in shots:
                if sh.collides_with(ast):
                    log_event("asteroid_shot")
                    sh.kill()
                    ast.split()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        #print(f"Delta time: {dt:.4f} seconds")

if __name__ == "__main__":
    main()
