import pygame
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Follow the Number")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Font
font = pygame.font.Font(None, 74)

# Membuat angka acak
numbers = list(range(1, 11))
random.shuffle(numbers)
positions = {}
for number in numbers:
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    positions[number] = (x, y)

# Game loop
running = True
clicked_numbers = []
lines = []

while running:
    screen.fill(white)

    # Menggambar angka
    for number, pos in positions.items():
        color = red if number in clicked_numbers else black
        text = font.render(str(number), True, color)
        screen.blit(text, pos)

        # Menggambar lingkaran di sekitar angka yang telah diklik
        if number in clicked_numbers:
            pygame.draw.circle(screen, blue, (pos[0] + text.get_width() // 2, pos[1] + text.get_height() // 2), text.get_width() // 2 + 10, 2)

    # Menggambar garis
    if len(clicked_numbers) > 1:
        for i in range(len(clicked_numbers) - 1):
            start_pos = positions[clicked_numbers[i]]
            end_pos = positions[clicked_numbers[i + 1]]
            pygame.draw.line(screen, blue, (start_pos[0] + 20, start_pos[1] + 30), (end_pos[0] + 20, end_pos[1] + 30), 5)

    # Menggambar pesan kemenangan
    if len(clicked_numbers) == len(numbers):
        win_text = font.render("You Win!", True, green)
        screen.blit(win_text, (width // 2 - win_text.get_width() // 2, height // 2 - win_text.get_height() // 2))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and len(clicked_numbers) < len(numbers):
            x, y = event.pos
            for number, pos in positions.items():
                rect = pygame.Rect(pos[0], pos[1], font.size(str(number))[0], font.size(str(number))[1])
                if rect.collidepoint(x, y):
                    if not clicked_numbers or number == clicked_numbers[-1] + 1:
                        clicked_numbers.append(number)
                    break

    pygame.display.flip()

pygame.quit()
