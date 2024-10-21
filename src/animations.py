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