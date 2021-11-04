import pygame

# https://www.spriters-resource.com/mobile/flappybird/sheet/59894/

from enum import Enum

class State(Enum):
    FLAPPING = 0
    FALLING = 1

class Bird(object):
    def __init__(self):
        self.image = pygame.image.load("pikachu.jpg").convert()
        self.rect = (0, 0, 200, 200)
        self.pos = (0, 100)
        self.queued_y_pos = 0
        self.state = State.FALLING

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.rect[2], self.rect[3])

    def flap(self):
        self.state = State.FLAPPING
        self.queued_y_pos = self.pos[1] - 30

    def move(self):
        if self.state == State.FLAPPING:
            if self.queued_y_pos < self.pos[1]:
                self.pos = (self.pos[0], self.pos[1] - 0.25)
            else:
                self.state = State.FALLING

        elif self.state == State.FALLING:
            self.pos = (self.pos[0], self.pos[1] + 0.25)

    def draw(self, screen):
        screen.blit(self.image, self.pos, self.rect)


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


bird = Bird()

# collision detect
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
# rect2 = pygame.Rect(0, 0, 75, 75)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if key pressed -> check if space bar was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()
        """
        # used this code to check which key i pressed
        if event.type == pygame.KEYDOWN:
            print(event.key)
        """

    screen.fill((255, 255, 255))

    bird.move()
    bird.draw(screen)

    # ????????????? need to look this up
    pygame.display.flip()

pygame.quit()