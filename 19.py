import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level 19 - Birthday Movie")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors (RGB)
BG_COLOR = (20, 24, 33)
WALL_COLOR = (30, 38, 56)
FLOOR_COLOR = (45, 55, 72)
TEXT_COLOR = (255, 255, 255)
GOLD_COLOR = (255, 215, 0)
PINK_COLOR = (255, 105, 180)
BLUE_COLOR = (70, 130, 185)
FLAME_COLOR = (255, 140, 0)
SMOKE_COLOR = (180, 180, 180)

# Fonts
font_large = pygame.font.SysFont("Arial", 42, bold=True)
font_medium = pygame.font.SysFont("Arial", 28, bold=True)
font_small = pygame.font.SysFont("Arial", 18)

# Confetti particles
confetti = []
for _ in range(150):
    confetti.append({
        'x': random.randint(0, WIDTH),
        'y': random.randint(-HEIGHT, 0),
        'color': random.choice([GOLD_COLOR, PINK_COLOR, BLUE_COLOR, (255, 0, 0), (0, 255, 0)]),
        'size': random.randint(4, 8),
        'speed': random.randint(2, 6)
    })

# Smoke particles
smoke_particles = []

def draw_pixel_character(surface, x, y, shirt_color, is_blinking=False):
    # Simple pixel art character representation
    # Head
    pygame.draw.rect(surface, (255, 220, 177), (x - 12, y - 35, 24, 24))
    # Hair
    pygame.draw.rect(surface, (50, 30, 10), (x - 14, y - 40, 28, 10))
    # Eyes
    if not is_blinking:
        pygame.draw.rect(surface, (0, 0, 0), (x - 6, y - 27, 4, 4))
        pygame.draw.rect(surface, (0, 0, 0), (x + 2, y - 27, 4, 4))
    # Shirt / Body
    pygame.draw.rect(surface, shirt_color, (x - 16, y - 11, 32, 26))
    # Pants
    pygame.draw.rect(surface, (40, 40, 80), (x - 14, y + 15, 12, 18))
    pygame.draw.rect(surface, (40, 40, 80), (x + 2, y + 15, 12, 18))

def main():
    start_ticks = pygame.time.get_ticks()
    candles_lit = True
    smoke_timer = 0

    running = True
    while running:
        # Calculate elapsed time in seconds
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- SCENE MANAGEMENT & RENDERING ---
        screen.fill(BG_COLOR)

        # Draw Room (Background)
        pygame.draw.rect(screen, WALL_COLOR, (0, 0, WIDTH, HEIGHT - 150))
        pygame.draw.rect(screen, FLOOR_COLOR, (0, HEIGHT - 150, WIDTH, 150))
        pygame.draw.line(screen, (15, 20, 30), (0, HEIGHT - 150), (WIDTH, HEIGHT - 150), 6)

        # Decorations (Balloons & Bunting)
        for i in range(6):
            bx = 100 + i * 120
            by = 80 + math.sin(seconds * 2 + i) * 10
            color = PINK_COLOR if i % 2 == 0 else BLUE_COLOR
            pygame.draw.circle(screen, color, (bx, int(by)), 20)
            pygame.draw.line(screen, (200, 200, 200), (bx, int(by) + 20), (bx, int(by) + 60), 1)

        # --- SCENE 1: Room setup & Main character in the middle with friends (0 - 4s) ---
        # --- SCENE 2: Friends bring the cake (4 - 8s) ---
        # --- SCENE 3: Blowing out candles (8 - 11s) ---
        # --- SCENE 4: Celebration & Level 19 Unlocked (11s+) ---

        if seconds < 4.0:
            scene_text = "Scene 1: Birthday Party Setup"
            # Main character in center
            draw_pixel_character(screen, WIDTH // 2, HEIGHT - 180, BLUE_COLOR)
            # Friends on sides
            draw_pixel_character(screen, WIDTH // 2 - 120, HEIGHT - 180, (50, 200, 100))
            draw_pixel_character(screen, WIDTH // 2 + 120, HEIGHT - 180, (220, 50, 50))

        elif seconds < 8.0:
            scene_text = "Scene 2: Bringing the Cake (19 Candles)"
            # Friends moving towards center carrying cake
            progress = (seconds - 4.0) / 4.0  # 0 to 1
            friend1_x = int(WIDTH // 2 - 120 + 80 * progress)
            friend2_x = int(WIDTH // 2 + 120 - 80 * progress)
            
            draw_pixel_character(screen, WIDTH // 2, HEIGHT - 180, BLUE_COLOR)
            draw_pixel_character(screen, friend1_x, HEIGHT - 180, (50, 200, 100))
            draw_pixel_character(screen, friend2_x, HEIGHT - 180, (220, 50, 50))

            # Cake in the middle
            cake_x, cake_y = WIDTH // 2, HEIGHT - 165
            pygame.draw.rect(screen, (240, 240, 240), (cake_x - 30, cake_y, 60, 30))
            pygame.draw.rect(screen, PINK_COLOR, (cake_x - 30, cake_y - 10, 60, 12))
            
            # Candles
            if candles_lit:
                for c in range(-9, 10):
                    cx = cake_x + c * 3
                    cy = cake_y - 18
                    pygame.draw.rect(screen, (255, 255, 255), (cx - 1, cy, 2, 8))
                    pygame.draw.circle(screen, FLAME_COLOR, (cx, cy - 2), 3)

        elif seconds < 11.0:
            scene_text = "Scene 3: Making a Wish..."
            # Main character steps closer to cake
            draw_pixel_character(screen, WIDTH // 2 - 20, HEIGHT - 180, BLUE_COLOR)
            draw_pixel_character(screen, WIDTH // 2 - 100, HEIGHT - 180, (50, 200, 100))
            draw_pixel_character(screen, WIDTH // 2 + 100, HEIGHT - 180, (220, 50, 50))

            # Cake & Smoke effect at second 9.5
            cake_x, cake_y = WIDTH // 2, HEIGHT - 165
            pygame.draw.rect(screen, (240, 240, 240), (cake_x - 30, cake_y, 60, 30))
            pygame.draw.rect(screen, PINK_COLOR, (cake_x - 30, cake_y - 10, 60, 12))

            if seconds > 9.5 and candles_lit:
                candles_lit = False
                # Create smoke particles
                for _ in range(20):
                    smoke_particles.append({
                        'x': cake_x + random.randint(-15, 15),
                        'y': cake_y - 20,
                        'vx': random.uniform(-1, 1),
                        'vy': random.uniform(-2, -0.5),
                        'alpha': 255
                    })

            if not candles_lit:
                # Render smoke
                for p in smoke_particles:
                    p['x'] += p['vx']
                    p['y'] += p['vy']
                    pygame.draw.circle(screen, SMOKE_COLOR, (int(p['x']), int(p['y'])), 4)

        else:
            scene_text = "Scene 4: Celebration!"
            # Characters celebrating (bouncing)
            bounce = int(math.sin(seconds * 10) * 5)
            draw_pixel_character(screen, WIDTH // 2, HEIGHT - 180 + bounce, BLUE_COLOR)
            draw_pixel_character(screen, WIDTH // 2 - 100, HEIGHT - 180 - bounce, (50, 200, 100))
            draw_pixel_character(screen, WIDTH // 2 + 100, HEIGHT - 180 - bounce, (220, 50, 50))

            # Render Confetti
            for p in confetti:
                p['y'] += p['speed']
                if p['y'] > HEIGHT:
                    p['y'] = random.randint(-50, 0)
                    p['x'] = random.randint(0, WIDTH)
                pygame.draw.rect(screen, p['color'], (p['x'], p['y'], p['size'], p['size']))

            # Display Birthday & Level 19 Text
            title_surf = font_large.render("HAPPY 19TH BIRTHDAY!", True, GOLD_COLOR)
            sub_surf = font_medium.render("LEVEL 19 UNLOCKED!", True, PINK_COLOR)
            
            screen.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2, 70))
            screen.blit(sub_surf, (WIDTH // 2 - sub_surf.get_width() // 2, 130))

        # Render subtle scene guide at bottom
        guide_surf = font_small.render(f"{scene_text} (Press Esc to Exit)", True, (120, 130, 150))
        screen.blit(guide_surf, (20, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()