import pygame
import pygame.transform as pt

#Sprite classes
class Neptune(pygame.sprite.Sprite):
    def __init__(self, x, y, i, scale):
        pygame.sprite.Sprite.__init__(self)

        img_x = 416 / scale  # 416
        img_y = 362 / scale  # 362

        #Images Load
        # Neptune Main Image
        raw_nep_main = pygame.image.load('assets/sprites/neptune_main.png')
        nep_main = pt.smoothscale(raw_nep_main, (img_x, img_y))  # (532,424)
        nep_main_t = pt.flip(nep_main, True, False)
        # Neptune Funny
        raw_nep_funny = pygame.image.load('assets/sprites/neptune_funny.png')
        nep_funny = pt.smoothscale(raw_nep_funny, (img_x, img_y))  # (532,424)
        nep_funny_t = pt.flip(nep_funny, True, False)
        # Neptune Wings
        raw_nep_hehe_w = pygame.image.load('assets/sprites/neptune_hehe_w.png')
        nep_hehe_w = pt.smoothscale(raw_nep_hehe_w, (img_x, img_y))  # (532,424)
        nep_hehe_w_t = pt.flip(nep_hehe_w, True, False)
        # Neptune Wings Blink
        raw_nep_hehe_w_c = pygame.image.load('assets/sprites/neptune_hehe_w_c.png')
        nep_hehe_w_c = pt.smoothscale(raw_nep_hehe_w_c, (img_x, img_y))  # (532,424)
        nep_hehe_w_c_t = pt.flip(nep_hehe_w_c, True, False)
        # Neptune Wings >_<
        raw_nep_v_v_w = pygame.image.load('assets/sprites/neptune_v_v_w.png')
        nep_v_v_w = pt.smoothscale(raw_nep_v_v_w, (img_x, img_y))  # (532,424)
        nep_v_v_w_t = pt.flip(nep_v_v_w, True, False)
        # Neptune >_<
        raw_nep_v_v = pygame.image.load('assets/sprites/neptune_v_v.png')
        nep_v_v = pt.smoothscale(raw_nep_v_v, (img_x, img_y))  # (532,424)
        nep_v_v_t = pt.flip(nep_v_v, True, False)

        #Idle Group
        self.nep = []
        self.nep.append(nep_main)
        self.nep.append(nep_v_v_t)
        self.nep.append(nep_main_t)
        self.nep.append(nep_v_v)

        #Blink_eye Group
        self.nep_blink = []
        self.nep_blink.append(nep_funny)
        self.nep_blink.append(nep_v_v_t)
        self.nep_blink.append(nep_funny_t)
        self.nep_blink.append(nep_v_v)

        #Flying Group
        self.hehe = []
        self.hehe.append(nep_hehe_w)
        self.hehe.append(nep_v_v_w_t)
        self.hehe.append(nep_hehe_w_t)
        self.hehe.append(nep_v_v_w)

        #Flying_blink Group
        self.hehe_blink = []
        self.hehe_blink.append(nep_hehe_w_c)
        self.hehe_blink.append(nep_v_v_w_t)
        self.hehe_blink.append(nep_hehe_w_c_t)
        self.hehe_blink.append(nep_v_v_w)

        self.images = self.nep
        self.index = i
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topright=(x, y))

        self.OPEN = 10  # maybe use an Enumerated Type
        self.CLOSE = 20
        self.anim = self.OPEN

    def update(self):
        #self.index += i
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def eyes_open(self):
        self.anim = self.OPEN

    def eyes_close(self):
        self.anim = self.CLOSE

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
        if self.anim == self.OPEN:
            self.images = self.hehe
        elif self.anim == self.CLOSE:
            self.images = self.hehe_blink

    def idle(self):
        if self.anim == self.OPEN:
            self.images = self.nep
        elif self.anim == self.CLOSE:
            self.images = self.nep_blink