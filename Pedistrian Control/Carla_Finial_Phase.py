import pygame
import random
import time

pygame.init()
WIDTH = 800
HEIGHT = 400
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car-Pedestrian Simulation")

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
car_x = 50
car_y = HEIGHT // 2
car_speed = 40

pedestrian_x = WIDTH - 50
pedestrian_y = HEIGHT - 30
pedestrian_speed = 10
start_time = time.time()
collision_time = 0.0
running = True
hit = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    car_x += car_speed / FPS
    pedestrian_y -= pedestrian_speed / FPS
    if car_x + 20 > pedestrian_x and car_y + 10 > pedestrian_y:
        hit = True
        if collision_time == 0.0:
            collision_time = time.time() - start_time
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 2 - 20, WIDTH, 40))
    for i in range(0, WIDTH, 40):
        pygame.draw.rect(screen, WHITE, (i, HEIGHT // 2 - 20, 20, 40))

    pygame.draw.rect(screen, BLACK, (car_x, car_y, 20, 10))  # Car
    pygame.draw.circle(screen, RED, (pedestrian_x, int(pedestrian_y)), 10)

    if hit:
        pygame.draw.line(screen, RED, (car_x, car_y), (pedestrian_x, int(pedestrian_y)), 2)

    elapsed_time = time.time() - start_time
    font = pygame.font.Font(None, 24)
    car_speed_text = font.render(f"Car Speed: {car_speed} km/h", True, BLACK)
    pedestrian_speed_text = font.render(f"Pedestrian Speed: {pedestrian_speed} km/h", True, BLACK)
    car_time_text = font.render(f"Car Time: {elapsed_time:.2f} seconds", True, BLACK)
    pedestrian_time_text = font.render(f"Pedestrian Time: {elapsed_time:.2f} seconds", True, BLACK)

    screen.blit(car_speed_text, (10, 10))
    screen.blit(pedestrian_speed_text, (10, 40))
    screen.blit(car_time_text, (10, 70))
    screen.blit(pedestrian_time_text, (10, 100))

    if hit:
        collision_time_text = font.render(f"Collision Time: {collision_time:.2f} seconds", True, RED)
        screen.blit(collision_time_text, (10, 130))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
