import pygame
import win32api
import win32con
import win32gui
import random
from pygame.locals import *
from sprites import Neptune
from animations import Flying_Animation
from animations import Idle_Animation
from set_interval import setInterval

def set_nep_timer(eventObj, interval):
    func = lambda x: pygame.event.post(x)
    return setInterval(func=func, sec=interval, args=[eventObj])

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Neptune Assistant")
    icon = pygame.image.load('assets/icons/Chell_Logo.ico')
    pygame.display.set_icon(icon)
    infoObject = pygame.display.Info()
    W = infoObject.current_w
    H = infoObject.current_h
    screen = pygame.display.set_mode((W, H - 20),pygame.NOFRAME) #,pygame.NOFRAME

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
    hb = H - 360 #450
    i = 0
    nep = Neptune(w, h, i)
    nep_group = pygame.sprite.Group(nep)
    idle_animation = Idle_Animation(wb, hb, nep.rect)
    flying_animation = Flying_Animation(wb, hb, nep.rect)
    #print(nep.rect)

    #Animation Switch Vars
    IDLE = 10  #maybe use an Enumerated Type
    FLYING = 20
    animation_state = IDLE
    ANIMATION_SWITCH = 1
    AnimationSwitchEvent = pygame.event.Event(USEREVENT, MyOwnType=ANIMATION_SWITCH)
    random_int = random.randint(6, 6)
    myIntervalHandle1 = set_nep_timer(AnimationSwitchEvent,random_int)

    #Main While
    running = True
    moving = False

    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                myIntervalHandle1.stop()
                running = False

            elif event.type == USEREVENT+1:
                nep.set_index()

            elif event.type == USEREVENT+2:
                nep.set_index()

            elif event.type == USEREVENT+3:
                animation_state = IDLE
                nep.zero_index()

            elif event.type == USEREVENT+4:
                nep.minus_index()

            elif event.type == USEREVENT:
                if event.MyOwnType == ANIMATION_SWITCH:
                    if animation_state == IDLE:
                        animation_state = FLYING
                    elif animation_state == FLYING:
                        animation_state = IDLE

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                myIntervalHandle1.stop()
                idle_animation.stop()
                #animation_state = IDLE
                if nep.rect.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP and event.button == 1:
                idle_animation.start()
                random_int = random.randint(6, 6)
                myIntervalHandle1 = set_nep_timer(AnimationSwitchEvent, random_int)
                moving = False

            elif event.type == MOUSEMOTION and moving:
                nep.rect.move_ip(event.rel)

        #Animation Switch
        if animation_state == IDLE:
            nep.idle()
            idle_animation.update()
        elif animation_state == FLYING:
            nep.flying()
            flying_animation.update()

        nep_group.update()
        screen.fill(t_color) #Transparent background
        clock.tick(FPS)
        nep_group.draw(screen)
        #screen.blit(nep.image, nep.rect)
        pygame.display.update()


if __name__ == '__main__':
    main()