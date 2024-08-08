import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load images
car_image = pygame.image.load('car.png')
tree_image = pygame.image.load('tree.png')
stone_image = pygame.image.load('stone.png')

# Scale images
car_image = pygame.transform.scale(car_image, (60, 120))
tree_image = pygame.transform.scale(tree_image, (60, 60))
stone_image = pygame.transform.scale(stone_image, (60, 60))

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoid the Trees and Stones")

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Game variables
car_x = SCREEN_WIDTH // 2 - car_image.get_width() // 2
car_y = SCREEN_HEIGHT - car_image.get_height() - 10
car_speed = 10

# Obstacle variables
obstacle_speed = 10
obstacle_frequency = 30  # Lower is more frequent
obstacles = []

# Function to create obstacles
def create_obstacle():
    obstacle_type = random.choice(['tree', 'stone'])
    x_pos = random.randint(0, SCREEN_WIDTH - tree_image.get_width())
    y_pos = -tree_image.get_height()
    if obstacle_type == 'tree':
        obstacles.append({'type': 'tree', 'x': x_pos, 'y': y_pos, 'image': tree_image})
    else:
        obstacles.append({'type': 'stone', 'x': x_pos, 'y': y_pos, 'image': stone_image})

# Function to move obstacles
def move_obstacles():
    for obstacle in obstacles:
        obstacle['y'] += obstacle_speed
    # Remove obstacles that have moved off the screen
    obstacles[:] = [ob for ob in obstacles if ob['y'] < SCREEN_HEIGHT]

# Function to draw everything on the screen
def draw():
    screen.fill(WHITE)
    screen.blit(car_image, (car_x, car_y))
    for obstacle in obstacles:
        screen.blit(obstacle['image'], (obstacle['x'], obstacle['y']))
    pygame.display.flip()

# Main game loop
def game_loop():
    global car_x
    frame_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_d] and car_x < SCREEN_WIDTH - car_image.get_width():
            car_x += car_speed

        if frame_count % obstacle_frequency == 0:
            create_obstacle()
        move_obstacles()

        draw()
        frame_count += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()