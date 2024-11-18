import pygame
import pygame.transform as pt

#Image Vars
img_x = 416
img_y = 362

#Neptune Main Image
raw_nep_main = pygame.image.load('assets/animation/neptune_main.png')
nep_main = pt.smoothscale(raw_nep_main, (img_x, img_y)) #(532,424)
nep_main_t = pt.flip(nep_main, True, False)
#Neptune >_<
raw_nep_v_v = pygame.image.load('assets/animation/neptune_v_v.png')
nep_v_v = pt.smoothscale(raw_nep_v_v, (img_x, img_y)) #(532,424)
nep_v_v_t = pt.flip(nep_v_v, True, False)

