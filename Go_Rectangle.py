import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Go Rectangle Go")

x=50
y=500
width = 20
height = 20
velocity = 10
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenWidth-width:
        x += velocity
    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y < screenHeight-height:
        y += velocity

    win.fill((0,0,0))
    pygame.draw.rect(win, (139, 157, 186), (x, y, width, height))
    pygame.display.update()

pygame.quit()
