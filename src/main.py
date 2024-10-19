import pygame
import win32api
import win32con
import win32gui
from pygame.locals import *
from sprites import Neptune
from animations import Bounce_Animation


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Neptune Assistant")
Icon = pygame.image.load('assets/icons/Chell_Logo.ico')
pygame.display.set_icon(Icon)
infoObject = pygame.display.Info()
W = infoObject.current_w
H = infoObject.current_h
screen = pygame.display.set_mode((W, H -10))#, pygame.NOFRAME

done = False
#Colors
Tcolor = (138,127,142)  # Transparency color
#windows on top

win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0,
                      win32con.SWP_NOMOVE |win32con.SWP_NOSIZE)
# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*Tcolor), 0, win32con.LWA_COLORKEY)


#Neptune Vars
#FPS = 30
w = W - 10
h = H - 500
wb = W - 500
hb = H - 450
nep = Neptune(w, h)
nep_group = pygame.sprite.Group(nep)
nep_group.update()
    #clock = pygame.time.Clock()

#bounce_animation = Bounce_Animation(screen, wb, hb, nep.rect)
FPS = 60
clock = pygame.time.Clock()

print(nep.rect)

#Main While
running = True
moving = False

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            print(nep.rect.x)
            if nep.rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP :
            moving = False

        elif event.type == MOUSEMOTION and moving:
            nep.rect.move_ip(event.rel)

    #bounce_animation.update()
    #bounce_animation.render()
    screen.fill(Tcolor)# Transparent background
    clock.tick(FPS)
    screen.blit(nep.image, nep.rect)
    pygame.display.update()
