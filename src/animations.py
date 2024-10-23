import random
from resourses import *

#Animation Triggers
bonk_event = pygame.USEREVENT + 1
no_bonk_event = pygame.USEREVENT + 2

#Flying Animation Class
class Flying_Animation():
    def __init__(self, wb,hb, nep_rect):
        self.rect = nep_rect
        self.wb = wb
        self.hb = hb
        self.NepPixel = 25
        self.nep_XChange = 3 * random.choice((-1, -1))
        self.nep_YChange = 3

    def update(self):
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
class Idle_Animation():
    def __init__(self, nep_rect):
        self.rect = nep_rect
        self.m = 1
        self.v = 5
        self.jump = 1

    def update(self):
        if self.jump == 1:
            k = 0.05 * self.m * self.v ** 2  # Calculate the vertical displacement
            self.rect.y -= k  # Update the sprite's vertical position
            self.v -= 1  # Simulate gravity by gradually decreasing velocity
            if self.v < 0:
                self.m = -1  # Change the direction of displacement for a realistic jump feel
            if self.v == -11:
                self.m = 1  # Reset parameters for subsequent jumps
                self.v = 10
                #self.jump = 0