"""
Made by ChatGPT 3.5
Conversation log: https://chat.openai.com/share/a5490967-ad95-4621-a5df-0bae1c9d955b
"""


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Player ship class
class Ship(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.modules = {'weapons': 100, 'ammo': 100, 'shields': 100, 'armor': 100}
        self.health = 100

    def draw_modules(self):
        font = pygame.font.Font(None, 36)
        for i, (module, value) in enumerate(self.modules.items()):
            text = font.render(f"{module}: {value}%", True, WHITE)
            screen.blit(text, (self.rect.x, self.rect.y + i * 30))

    def draw_healthbar(self):
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 20, self.health, 10))


# Clickable button class
class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        text_render = self.font.render(self.text, True, RED)
        screen.blit(text_render, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 10

    def update(self):
        angle = pygame.math.Vector2(self.target_x - self.rect.x, self.target_y - self.rect.y).angle_to((1, 0))
        self.rect.x += self.speed * pygame.math.Vector2(1, 0).rotate(angle).x
        self.rect.y += self.speed * pygame.math.Vector2(1, 0).rotate(angle).y


# Fire animation class
class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.Surface((20, 20)), pygame.Surface((30, 30))]
        for image in self.images:
            image.fill(YELLOW)
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame_duration = 5
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter == self.frame_duration:
            self.frame_counter = 0
            self.image_index += 1
            if self.image_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.image_index]


# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle Game")
clock = pygame.time.Clock()

# Create player ships
player_ship = Ship(BLUE, 50, 300)
enemy_ship = Ship(RED, 700, 300)

# Create fire button
fire_button = Button(WHITE, WIDTH - 150, HEIGHT - 80, 120, 50, "Fire")

# Group for all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player_ship, enemy_ship, fire_button)

# Group for bullets
bullets = pygame.sprite.Group()

# Group for fire animations
fire_animations = pygame.sprite.Group()

# Main game loop
running = True
player_turn = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the fire button is clicked during the player's turn
            if player_turn and fire_button.is_clicked(event.pos):
                # Implement firing action
                target_x, target_y = enemy_ship.rect.center
                bullet = Bullet(player_ship.rect.x, player_ship.rect.y, target_x, target_y)
                bullets.add(bullet)

                # Create and add fire animation
                fire_animation = Fire(player_ship.rect.x - 5, player_ship.rect.y - 5)
                fire_animations.add(fire_animation)

                player_turn = False

    # Update bullets
    bullets.update()

    # Update fire animations
    fire_animations.update()

    # Enemy's turn
    if not player_turn:
        # Implement actions for enemy's turn (similar to player's turn)
        random_module = random.choice(list(enemy_ship.modules.keys()))
        enemy_ship.modules[random_module] -= random.randint(10, 30)
        enemy_ship.modules[random_module] = max(enemy_ship.modules[random_module], 0)
        player_turn = True

    # Draw everything
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Draw modules for player and enemy ships
    player_ship.draw_modules()
    enemy_ship.draw_modules()

    # Draw health bars
    player_ship.draw_healthbar()
    enemy_ship.draw_healthbar()

    # Draw fire button
    fire_button.draw()

    # Draw and update bullets
    bullets.draw(screen)

    # Draw and update fire animations
    fire_animations.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
