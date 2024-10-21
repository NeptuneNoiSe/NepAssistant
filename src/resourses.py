import pygame
import pygame.transform as pt

#Neptune Main Image
raw_nep_main = pygame.image.load('assets/animation/neptune_main.png')
nep_main = pt.smoothscale(raw_nep_main, (432, 324)) #(532,424)
nep_main_t = pt.flip(nep_main, True, False)
#Neptune >_<
raw_nep_v_v = pygame.image.load('assets/animation/neptune_v_v.png')
nep_v_v = pt.smoothscale(raw_nep_v_v, (432, 324)) #(532,424)
nep_v_v_t = pt.flip(nep_v_v, True, False)

