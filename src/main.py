import pygame
import win32api
import win32con
import win32gui
from pygame.locals import *
from sprites import Neptune
from animations import Flying_Animation
from animations import Idle_Animation

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Neptune Assistant")
    icon = pygame.image.load('assets/icons/Chell_Logo.ico')
    pygame.display.set_icon(icon)
    infoObject = pygame.display.Info()
    W = infoObject.current_w
    H = infoObject.current_h
    screen = pygame.display.set_mode((W, H - 10)) #,pygame.NOFRAME

    #Colors
    t_color = (138, 127, 142) #Transparency color

    #Windows on top
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    #Create layered window
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

    #Set window transparency color
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*t_color), 0, win32con.LWA_COLORKEY)

    #Neptune Vars
    clock = pygame.time.Clock()
    FPS = 30
    w = W - 25
    h = H - 420
    wb = W - 400 #500
    hb = H - 350 #450
    DOUBLECLICKTIME = 500
    i = 0
    nep = Neptune(w, h, i)
    nep_group = pygame.sprite.Group(nep)
    idle_animation = Idle_Animation(nep.rect)
    flying_animation = Flying_Animation(wb, hb, nep.rect)
    #print(nep.rect)

    #Main While
    running = True
    moving = False

    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                running = False

            elif event.type == USEREVENT+1:
                    nep.set_index()

            elif event.type == USEREVENT+2:
                    nep.set_index()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if nep.rect.collidepoint(event.pos):
                    moving = True


                if clock.tick() < DOUBLECLICKTIME:
                    nep.zero_index()
                    #print(nep.rect)
                    #return flying_animation.update()
                    idle_animation.update()

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                nep.rect.move_ip(event.rel)

        idle_animation.update()
        #flying_animation.update()
        nep_group.update()
        screen.fill(t_color) #Transparent background
        clock.tick(FPS)
        nep_group.draw(screen)
        #screen.blit(nep.image, nep.rect)
        pygame.display.update()


if __name__ == '__main__':
    main()