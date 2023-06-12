import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the simulation window
WIDTH = 800
HEIGHT = 400
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car-Pedestrian Simulation")

clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the car and pedestrian
car_x = 50
car_y = HEIGHT // 2
car_speed = 40

pedestrian_x = WIDTH - 50
pedestrian_y = HEIGHT // 2
pedestrian_speed = 5

# Main simulation loop
running = True
hit = False

while running:
    # Process input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the car and pedestrian positions
    car_x += car_speed / FPS
    pedestrian_x -= pedestrian_speed / FPS

    # Check for collision
    if abs(car_x - pedestrian_x) < 20 and abs(car_y - pedestrian_y) < 20:
        hit = True

    # Render the scene
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (car_x, car_y, 20, 10))  # Car
    pygame.draw.circle(screen, RED, (pedestrian_x, pedestrian_y), 10)  # Pedestrian

    if hit:
        pygame.draw.line(screen, RED, (car_x, car_y), (pedestrian_x, pedestrian_y), 2)  # Collision line

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit the simulation
pygame.quit()
