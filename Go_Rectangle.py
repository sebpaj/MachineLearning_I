import pygame
from tkinter import messagebox

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Go Rectangle Go")

background = pygame.image.load("images/background.png")
character = pygame.image.load("images/champion.png")
winner = pygame.image.load("images/winner.png")
clock = pygame.time.Clock()


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.hitbox = self.x, self.y, self.width, self.height

    def draw(self, win):
        win.blit(character, (self.x, self.y))
        self.hitbox = self.x, self.y, self.width, self.height


class Obstacles(object):
    obstacles_img = [pygame.image.load("images/obstacle1.png"), pygame.image.load("images/obstacle2.png"),
                     pygame.image.load("images/obstacle3.png"), pygame.image.load("images/obstacle4.png")]

    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.w1, self.h1 = self.obstacles_img[0].get_rect().size
        self.w2, self.h2 = self.obstacles_img[1].get_rect().size
        self.w3, self.h3 = self.obstacles_img[2].get_rect().size
        self.w4, self.h4 = self.obstacles_img[3].get_rect().size
        self.hitbox0 = self.x, self.y, self.w1, self.h1
        self.hitbox1 = self.x, self.y, self.w2, self.h2
        self.hitbox2 = self.x, self.y, self.w3, self.h3
        self.hitbox3 = self.x, self.y, self.w4, self.h4

    def draw(self, win):
        win.blit(self.obstacles_img[self.index], (self.x, self.y))
        if self.index == 0:
            self.hitbox = self.hitbox0
        elif self.index == 1:
            self.hitbox = self.hitbox1
        elif self.index == 2:
            self.hitbox = self.hitbox2
        elif self.index == 3:
            self.hitbox = self.hitbox3


def redrawGameWindow():
    win.blit(background, (0, 0))
    win.blit(winner, (700, 0))
    champion.draw(win)
    obstacles0.draw(win)
    obstacles1.draw(win)
    obstacles2.draw(win)
    obstacles3.draw(win)
    obstacles4.draw(win)
    obstacles5.draw(win)
    obstacles6.draw(win)
    obstacles7.draw(win)
    obstacles8.draw(win)
    obstacles9.draw(win)
    obstacles10.draw(win)
    obstacles11.draw(win)
    obstacles12.draw(win)
    obstacles13.draw(win)
    obstacles14.draw(win)
    pygame.display.update()

#change for rect for colission detection
def get_rect(rect):
    return pygame.Rect(rect)

def check_has_won(rect):
    if rect[0] >= 700 and rect[1] <= 80:
        messagebox.showinfo("Congratulations", "You won the game!")
        champion.x = 50
        champion.y = 500

#mainloop
has_won = False
run = True
champion = Player(50, 500, 20, 20)
obstacles0 = Obstacles(0, 100, 450)
obstacles1 = Obstacles(1, 200, 460)
obstacles2 = Obstacles(2, 300, 350)
obstacles3 = Obstacles(3, 100, 300)
obstacles4 = Obstacles(0, 400, 300)
obstacles5 = Obstacles(0, 500, 300)
obstacles6 = Obstacles(3, 500, 300)
obstacles7 = Obstacles(2, 600, 350)
obstacles8 = Obstacles(1, 50, 50)
obstacles9 = Obstacles(0, 150, 50)
obstacles10 = Obstacles(1, 250, 50)
obstacles11 = Obstacles(3, 260, 250)
obstacles12 = Obstacles(3, 260, 180)
obstacles13 = Obstacles(0, 450, 0)
obstacles14 = Obstacles(0, 650, 100)

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if any([get_rect(champion.hitbox).colliderect(get_rect(obstacles0.hitbox0)), get_rect(champion.hitbox).colliderect(get_rect(obstacles1.hitbox1)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles2.hitbox2)), get_rect(champion.hitbox).colliderect(get_rect(obstacles3.hitbox3)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles4.hitbox0)), get_rect(champion.hitbox).colliderect(get_rect(obstacles5.hitbox0)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles6.hitbox3)), get_rect(champion.hitbox).colliderect(get_rect(obstacles7.hitbox2)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles8.hitbox1)), get_rect(champion.hitbox).colliderect(get_rect(obstacles9.hitbox0)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles10.hitbox0)), get_rect(champion.hitbox).colliderect(get_rect(obstacles11.hitbox3)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles12.hitbox3)), get_rect(champion.hitbox).colliderect(get_rect(obstacles13.hitbox0)),
            get_rect(champion.hitbox).colliderect(get_rect(obstacles14.hitbox0))]):
        champion.x, champion.y = 50, 500
    else:
        if keys[pygame.K_LEFT] and champion.x > 0:
            champion.x -= champion.velocity
        if keys[pygame.K_RIGHT] and champion.x < screenWidth - champion.width:
            champion.x += champion.velocity
        if keys[pygame.K_UP] and champion.y > 0:
            champion.y -= champion.velocity
        if keys[pygame.K_DOWN] and champion.y < screenHeight - champion.height:
            champion.y += champion.velocity

    check_has_won(champion.hitbox)
    redrawGameWindow()


pygame.quit()
