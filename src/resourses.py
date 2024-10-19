import pygame
import pygame.transform as pt

#Neptune Main Image
raw_nep_main = pygame.image.load('assets/animation/neptune_main.png')
nep_main = pt.smoothscale(raw_nep_main, (532, 424))
nep_main_t = pt.flip(nep_main, True, False)

