from resourses import *
#Sprite classes
class Neptune(pygame.sprite.Sprite):
    def __init__(self, x, y, i):
        pygame.sprite.Sprite.__init__(self)
        #Idle Group
        self.nep = []
        self.nep.append(nep_main)
        self.nep.append(nep_v_v_t)
        self.nep.append(nep_main_t)
        self.nep.append(nep_v_v)
        #Flying Group
        self.hehe = []
        self.hehe.append(nep_hehe_w)
        self.hehe.append(nep_v_v_w_t)
        self.hehe.append(nep_hehe_w_t)
        self.hehe.append(nep_v_v_w)

        self.images = self.nep
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

    def minus_index(self):
        self.index -= 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def zero_index(self):
        self.index = 0

    def flying(self):
        self.images = self.hehe

    def idle(self):
        self.images = self.nep