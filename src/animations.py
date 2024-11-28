import random
from resourses import *

#Animation Triggers
bonk_event = pygame.USEREVENT + 1
no_bonk_event = pygame.USEREVENT + 2
border_event = pygame.USEREVENT + 3
minus_event = pygame.USEREVENT + 4

#Flying Animation Class
class Flying_Animation:
    def __init__(self, wb,hb, nep_rect):
        self.rect = nep_rect
        self.wb = wb
        self.hb = hb
        self.NepPixel = 25
        self.nep_XChange = 3 * -1 #random.choice((-1, -1))
        self.nep_YChange = 3

    def update(self):
        if self.rect.x > self.wb or self.rect.y > self.hb:
            self.rect.x = self.wb / 2
            self.rect.y = self.hb / 2
            self.nep_XChange = 3 * -1
            self.nep_YChange = 3
            pygame.time.set_timer(border_event, 1, 1)

        if self.rect.x < -3 or self.rect.y < -3:
            self.rect.x = self.wb / 2
            self.rect.y = self.hb / 2
            self.nep_XChange = 3 * -1
            self.nep_YChange = 3
            pygame.time.set_timer(border_event, 1, 1)

        if self.rect.x + self.NepPixel >= self.wb or self.rect.x <= 0:
            self.nep_XChange *= -1
            pygame.time.set_timer(bonk_event, 1,1)
            print('Я Ударилась >_<')
            pygame.time.set_timer(no_bonk_event, 1000,1)

        if self.rect.y + self.NepPixel >= self.hb or self.rect.y <= 0:
            self.nep_YChange *= -1

        self.rect.x += self.nep_XChange
        self.rect.y += self.nep_YChange

#Idle Animation
class Idle_Animation:
    def __init__(self, wb,hb, nep_rect):
        self.rect = nep_rect
        self.wb = wb
        self.hb = hb
        self.nep_YChange = 3
        self.m = 1
        self.v = 5
        self.jump = 1
        self.i = 1
        self.k = 0

    def update(self):
        if self.rect.y <= self.hb - 63:
            self.jump = 0
            self.nep_YChange *= 1

            self.rect.y += self.nep_YChange
        if self.i == 1:
            pygame.time.set_timer(minus_event, 1, 1)
            self.i = 0
            self.k = 1

        if self.rect.y >= self.hb - 63:
            self.jump = 1
            if self.k == 1 :
                pygame.time.set_timer(bonk_event, 1, 1)
                self.k = 0
                self.i = 1

        if self.jump == 1:
            k = 0.05 * self.m * self.v ** 2  # Calculate the vertical displacement
            self.rect.y -= k  # Update the sprite's vertical position
            self.v -= 1  # Simulate gravity by gradually decreasing velocity
            if self.v < 0:
                self.m = -1  # Change the direction of displacement for a realistic jump feel
            if self.v == -11:
                self.m = 1  # Reset parameters for subsequent jumps
                self.v = 10

    def start(self):
        self.jump = 1

    def stop(self):
        self.jump = 0
