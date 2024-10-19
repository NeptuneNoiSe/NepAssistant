from resourses import *
#Sprite class
class Neptune(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(nep_main)
        self.images.append(nep_main_t)

        self.index = 1
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topright=(x, y))

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]