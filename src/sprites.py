import pygame
import pygame.transform as pt

# Sprite classes
class Neptune_Face(pygame.sprite.Sprite):
    def __init__(self, x, y, i, scale):
        pygame.sprite.Sprite.__init__(self)
        # Image Resolution
        img_x = 416 / scale  # 416
        img_y = 362 / scale  # 362

        # Images Load
        # Neptune Main Face
        raw_nep_face = pygame.image.load('assets/sprites/nep_face_idle.png')
        nep_face = pt.smoothscale(raw_nep_face, (img_x, img_y))  # (532,424)
        nep_face_t = pt.flip(nep_face, True, False)
        # Neptune Funny Face
        raw_nep_face_funny = pygame.image.load('assets/sprites/nep_face_funny.png')
        nep_face_funny = pt.smoothscale(raw_nep_face_funny, (img_x, img_y))  # (532,424)
        nep_face_funny_t = pt.flip(nep_face_funny, True, False)
        # Neptune HeHe Face
        raw_nep_face_hehe = pygame.image.load('assets/sprites/nep_face_hehe.png')
        nep_face_hehe = pt.smoothscale(raw_nep_face_hehe, (img_x, img_y))  # (532,424)
        nep_face_hehe_t = pt.flip(nep_face_hehe, True, False)
        # Neptune HeHe Face Blink
        raw_nep_face_hehe_c = pygame.image.load('assets/sprites/nep_face_hehe_c.png')
        nep_face_hehe_c = pt.smoothscale(raw_nep_face_hehe_c, (img_x, img_y))  # (532,424)
        nep_face_hehe_c_t = pt.flip(nep_face_hehe_c, True, False)
        # Neptune >_< Face
        raw_nep_face_v_v = pygame.image.load('assets/sprites/nep_face_v_v.png')
        nep_face_v_v = pt.smoothscale(raw_nep_face_v_v, (img_x, img_y))  # (532,424)
        nep_face_v_v_t = pt.flip(nep_face_v_v, True, False)

        # Idle Group
        self.nep = []
        self.nep.append(nep_face)
        self.nep.append(nep_face_v_v_t)
        self.nep.append(nep_face_t)
        self.nep.append(nep_face_v_v)

        # Blink_eye Group
        self.nep_blink = []
        self.nep_blink.append(nep_face_funny)
        self.nep_blink.append(nep_face_v_v_t)
        self.nep_blink.append(nep_face_funny_t)
        self.nep_blink.append(nep_face_v_v)

        # Flying Group
        self.hehe = []
        self.hehe.append(nep_face_hehe)
        self.hehe.append(nep_face_v_v_t)
        self.hehe.append(nep_face_hehe_t)
        self.hehe.append(nep_face_v_v)

        # Flying_blink Group
        self.hehe_blink = []
        self.hehe_blink.append(nep_face_hehe_c)
        self.hehe_blink.append(nep_face_v_v_t)
        self.hehe_blink.append(nep_face_hehe_c_t)
        self.hehe_blink.append(nep_face_v_v)

        # Sprites Vars
        self.images = self.nep
        self.index = i
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topright=(x, y))

        # Switch Vars
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

class Neptune_Body(pygame.sprite.Sprite):
    def __init__(self, x, y, i, scale):
        pygame.sprite.Sprite.__init__(self)
        # Image Resolution
        img_x = 416 / scale  # 416
        img_y = 362 / scale  # 362

        # Images Load
        # Neptune Main Image
        raw_nep_main = pygame.image.load('assets/sprites/neptune_main.png')
        nep_main = pt.smoothscale(raw_nep_main, (img_x, img_y))  # (532,424)
        nep_main_t = pt.flip(nep_main, True, False)

        # Idle Group
        self.nep = []
        self.nep.append(nep_main)
        self.nep.append(nep_main_t)
        self.nep.append(nep_main_t)
        self.nep.append(nep_main)

        # Sprites Vars
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

class Neptune_Wings(pygame.sprite.Sprite):
    def __init__(self, x, y, i, scale):
        pygame.sprite.Sprite.__init__(self)
        # Image Resolution
        img_x = 416 / scale  # 416
        img_y = 362 / scale  # 362

        # Images Load
        # Neptune Blank Image
        raw_nep_blank = pygame.image.load('assets/sprites/nep_blank.png')
        nep_blank = pt.smoothscale(raw_nep_blank, (img_x, img_y))  # (532,424)

        # Neptune Wings
        raw_nep_wings = pygame.image.load('assets/sprites/nep_wings.png')
        nep_wings = pt.smoothscale(raw_nep_wings, (img_x, img_y))  # (532,424)
        nep_wings_t = pt.flip(nep_wings, True, False)

        # Blank Group
        self.nep_blank = []
        self.nep_blank.append(nep_blank)
        self.nep_blank.append(nep_blank)
        self.nep_blank.append(nep_blank)
        self.nep_blank.append(nep_blank)

        # Wings Group
        self.nep_wings = []
        self.nep_wings.append(nep_wings)
        self.nep_wings.append(nep_wings_t)
        self.nep_wings.append(nep_wings_t)
        self.nep_wings.append(nep_wings)

        # Sprites Vars
        self.images = self.nep_blank
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
        self.images = self.nep_wings

    def idle(self):
        self.images = self.nep_blank

class Neptune_Guns(pygame.sprite.Sprite):
    def __init__(self, x, y, i, scale):
        pygame.sprite.Sprite.__init__(self)
        # Image Resolution
        img_x = 416 / scale  # 416
        img_y = 362 / scale  # 362

        # Images Load
        # Neptune Main Image
        raw_nep_blank = pygame.image.load('assets/sprites/nep_blank.png')
        nep_blank = pt.smoothscale(raw_nep_blank, (img_x, img_y))  # (532,424)

        raw_nep_guns = pygame.image.load('assets/sprites/nep_guns.png')
        nep_guns = pt.smoothscale(raw_nep_guns, (img_x, img_y))  # (532,424)
        nep_guns_t = pt.flip(nep_guns, True, False)

        # Blank Group
        self.nep_blank = []
        self.nep_blank.append(nep_blank)
        self.nep_blank.append(nep_blank)
        self.nep_blank.append(nep_blank)
        self.nep_blank.append(nep_blank)

        # Guns Group
        self.nep_guns = []
        self.nep_guns.append(nep_guns)
        self.nep_guns.append(nep_guns_t)
        self.nep_guns.append(nep_guns_t)
        self.nep_guns.append(nep_guns)

        # Sprites Vars
        self.images = self.nep_blank
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
        self.images = self.nep_guns

    def idle(self):
        self.images = self.nep_blank