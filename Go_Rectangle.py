import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Go Rectangle Go")

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5


def redrawGameWindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (139, 157, 186), (champion.x, champion.y, champion.width, champion.height))
    pygame.display.update()


run = True
champion = Player(50, 500, 20, 20)
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and champion.x > 0:
        champion.x -= champion.velocity
    if keys[pygame.K_RIGHT] and champion.x < screenWidth-champion.width:
        champion.x += champion.velocity
    if keys[pygame.K_UP] and champion.y > 0:
        champion.y -= champion.velocity
    if keys[pygame.K_DOWN] and champion.y < screenHeight-champion.height:
        champion.y += champion.velocity

    redrawGameWindow()

pygame.quit()
