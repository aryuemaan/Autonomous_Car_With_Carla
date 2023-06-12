import pygame
import random
import time

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

# Get the current time
start_time = time.time()

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
        collision_time = time.time() - start_time

    # Render the scene
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (car_x, car_y, 20, 10))  # Car
    pygame.draw.circle(screen, RED, (pedestrian_x, pedestrian_y), 10)  # Pedestrian

    if hit:
        pygame.draw.line(screen, RED, (car_x, car_y), (pedestrian_x, pedestrian_y), 2)  # Collision line

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Display car and pedestrian speeds and times
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

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit the simulation
pygame.quit()