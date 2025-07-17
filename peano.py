import pygame
import math
import colorsys

# Initialize Pygame
pygame.init()

# Get screen info and set up fullscreen
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Peano Curve Animation")

# Colors
BLACK = (0, 0, 0)

class PeanoCurve:
    def __init__(self):
        self.current_iteration = 0
        self.max_iterations = 4  # Peano grows very quickly, so fewer iterations needed
        self.animation_speed = 0.02
        self.animation_progress = 0
        self.color_hue = 0
        self.scale_factor = 0.8
        self.min_scale = 0.0001
        self.max_scale = 5.0
        self.zoom_speed = 0.1
        self.offset_x = 0
        self.offset_y = 0
        self.move_speed = 20
        self.last_zoom_time = 0
        self.last_move_time = 0
        self.zoom_delay = 200
        self.move_delay = 200
        
    def generate_peano(self, x, y, size, iteration, direction=1):
        if iteration == 0:
            return [(x, y)]
        
        points = []
        third_size = size / 3
        
        # Generate the nine points for the Peano curve
        # The direction parameter determines the orientation of the curve
        if direction == 1:
            # Clockwise pattern
            points.extend(self.generate_peano(x - third_size, y - third_size, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x, y - third_size, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x + third_size, y - third_size, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x + third_size, y, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x + third_size, y + third_size, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x, y + third_size, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x - third_size, y + third_size, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x - third_size, y, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x, y, third_size, iteration - 1, 1))
        else:
            # Counter-clockwise pattern
            points.extend(self.generate_peano(x - third_size, y - third_size, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x - third_size, y, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x - third_size, y + third_size, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x, y + third_size, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x + third_size, y + third_size, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x + third_size, y, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x + third_size, y - third_size, third_size, iteration - 1, -1))
            points.extend(self.generate_peano(x, y - third_size, third_size, iteration - 1, 1))
            points.extend(self.generate_peano(x, y, third_size, iteration - 1, -1))
        
        return points
    
    def update(self, zoom_in=False, zoom_out=False, move_x=0, move_y=0):
        current_time = pygame.time.get_ticks()
        
        # Handle zoom with delay
        if (zoom_in or zoom_out) and (current_time - self.last_zoom_time) > self.zoom_delay:
            if zoom_in:
                self.scale_factor = min(self.max_scale, 
                                      self.scale_factor + self.zoom_speed)
            elif zoom_out:
                self.scale_factor = max(self.min_scale, 
                                      self.scale_factor - self.zoom_speed)
            self.last_zoom_time = current_time
        
        # Handle movement with delay
        if (move_x != 0 or move_y != 0) and (current_time - self.last_move_time) > self.move_delay:
            self.offset_x += move_x * self.move_speed
            self.offset_y += move_y * self.move_speed
            self.last_move_time = current_time
        
        self.animation_progress += self.animation_speed
        if self.animation_progress >= 1:
            self.animation_progress = 0
            self.current_iteration = min(self.current_iteration + 1, self.max_iterations)
        
        self.color_hue = (self.color_hue + 0.001) % 1.0
    
    def draw(self, screen):
        # Draw background
        screen.fill(BLACK)
        
        # Calculate the size of the initial square
        size = min(WIDTH, HEIGHT) * self.scale_factor * 0.8
        
        # Generate points for current iteration
        points = self.generate_peano(
            WIDTH/2 + self.offset_x,
            HEIGHT/2 + self.offset_y,
            size,
            self.current_iteration
        )
        
        # Draw lines with color gradient
        for i in range(len(points) - 1):
            progress = i / (len(points) - 1)
            hue = (self.color_hue + progress * 0.3) % 1.0
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            color = tuple(int(c * 255) for c in rgb)
            
            # Draw line with glow effect
            for width in range(3, 0, -1):
                alpha = int(255 * (width / 3))
                glow_color = (*color, alpha)
                pygame.draw.line(screen, glow_color, points[i], points[i + 1], width)

def main():
    clock = pygame.time.Clock()
    fractal = PeanoCurve()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        move_x = 0
        move_y = 0
        
        # WASD movement
        if keys[pygame.K_a]: move_x -= 1
        if keys[pygame.K_d]: move_x += 1
        if keys[pygame.K_w]: move_y -= 1
        if keys[pygame.K_s]: move_y += 1
        
        # Arrow key zoom
        zoom_in = keys[pygame.K_UP]
        zoom_out = keys[pygame.K_DOWN]
        
        fractal.update(zoom_in=zoom_in, zoom_out=zoom_out, 
                      move_x=move_x, move_y=move_y)
        fractal.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main() 