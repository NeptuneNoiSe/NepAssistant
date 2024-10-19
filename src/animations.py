import random
from resourses import nep_main

#Bounce Animation Class
class Bounce_Animation():
    def __init__(self,screen, wb,hb, nep_rect):
        self.screen = screen
        self.nep_main = nep_main
        self.rect = nep_rect
        self.wb = wb
        self.hb = hb
        self.NepPixel = 24
        self.nep_XChange = 3 * random.choice((1, -1))
        self.nep_YChange = 3

    def update(self):
        if self.rect.x + self.NepPixel >= self.wb or self.rect.x <= 0:
            self.nep_XChange *= -1

        if self.rect.y + self.NepPixel >= self.hb or self.rect.y <= 0:
            self.nep_YChange *= -1

        self.rect.x += self.nep_XChange
        self.rect.y += self.nep_YChange

    def render(self):
        self.screen.blit(self.nep_main, self.rect)
