import pygame

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Circle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # White background

    # Draw circle with adjustable parameters
    center_x = screen_width // 2
    center_y = screen_height // 2
    radius = 100  # Adjust as needed
    color = (0, 0, 255)  # Blue color

    pygame.draw.circle(screen, color, (center_x, center_y), radius)

    pygame.display.flip()

pygame.quit()
