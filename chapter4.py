import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('example.jpg')

# Loop utama permainan
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 1
    if x > 800:
        x = 0

    # Menggambar gambar
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Memuat suara
    sound = pygame.mixer.Sound('result.wav')

    # Memutar suara
    sound.play()

pygame.quit()