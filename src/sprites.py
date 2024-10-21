from resourses import *
#Sprite classes
class Neptune(pygame.sprite.Sprite):
    def __init__(self, x, y, i):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(nep_main)
        self.images.append(nep_v_v_t)
        self.images.append(nep_main_t)
        self.images.append(nep_v_v)
        self.index = i
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topright=(x, y))

    def update(self):
        #self.index += i
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def set_index(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def zero_index(self):
        self.index = 0