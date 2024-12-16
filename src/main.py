import pygame
import win32api
import win32con
import win32gui
import random
from pygame.locals import *
from sprites import Neptune_Face, Neptune_Body, Neptune_Wings, Neptune_Guns
from animations import Flying_Animation, Idle_Animation
from effects import ParticleSystem
from set_interval import setInterval

#Timer Function
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
    scale = 1.3
    rand_a = 10
    rand_b = 10
    blink_int = random.randint(3, 9)
    w = W - 25/scale
    h = H - 420/scale
    wb = W - 400/scale #500
    hb = H - 360/scale #450
    i = 0

    #Initial Sprites
    nep_face = Neptune_Face(w, h, i, scale)
    nep_body = Neptune_Body(w, h, i, scale)
    nep_wings = Neptune_Wings(w, h, i, scale)
    nep_guns = Neptune_Guns(w, h, i, scale)
    nep_group_fly = pygame.sprite.Group(nep_wings, nep_guns)
    nep_group_main = pygame.sprite.Group(nep_body, nep_face)

    #Initial Animation
    idle_animation_face = Idle_Animation(wb, hb, nep_face.rect)
    idle_animation_body = Idle_Animation(wb, hb, nep_body.rect)
    idle_animation_wings = Idle_Animation(wb, hb, nep_wings.rect)
    idle_animation_guns = Idle_Animation(wb, hb, nep_guns.rect)
    flying_animation_face = Flying_Animation(wb, hb, nep_face.rect)
    flying_animation_body = Flying_Animation(wb, hb, nep_body.rect)
    flying_animation_wings = Flying_Animation(wb, hb, nep_wings.rect)
    flying_animation_guns = Flying_Animation(wb, hb, nep_guns.rect)

    #Initial Particle System
    particle_system = ParticleSystem()

    #Animation Switch Vars
    IDLE = 10  #maybe use an Enumerated Type
    FLYING = 20
    animation_state = IDLE
    ANIMATION_SWITCH = 1
    CLOSE_EYES_SWITCH = 2
    OPEN_EYES_SWITCH = 3

    #Timer Events
    AnimationSwitchEvent = pygame.event.Event(USEREVENT, MyOwnType=ANIMATION_SWITCH)
    CloseEyesEvent = pygame.event.Event(USEREVENT, MyOwnType=CLOSE_EYES_SWITCH)
    OpenEyesEvent = pygame.event.Event(USEREVENT, MyOwnType=OPEN_EYES_SWITCH)
    random_int = random.randint(rand_a, rand_b)

    #Set Timer Interval
    AnimationSwitchInterval = set_nep_timer(AnimationSwitchEvent,random_int)
    CloseEyesInterval = set_nep_timer(CloseEyesEvent, blink_int)
    OpenEyesInterval = set_nep_timer(OpenEyesEvent, 0.25)
    OpenEyesInterval.stop()

    #Group Functions
    def nep_set_index():
        nep_face.set_index()
        nep_body.set_index()
        nep_wings.set_index()
        nep_guns.set_index()

    def nep_zero_index():
        nep_face.zero_index()
        nep_body.zero_index()
        nep_wings.zero_index()
        nep_guns.zero_index()

    def nep_minus_index():
        nep_face.minus_index()
        nep_body.minus_index()
        nep_wings.minus_index()
        nep_guns.minus_index()

    def idle_animation_stop():
        idle_animation_face.stop()
        idle_animation_body.stop()
        idle_animation_wings.stop()
        idle_animation_guns.stop()

    def idle_animation_start():
        idle_animation_face.start()
        idle_animation_body.start()
        idle_animation_wings.start()
        idle_animation_guns.start()

    def nep_rect_move():
        nep_face.rect.move_ip(event.rel)
        nep_body.rect.move_ip(event.rel)
        nep_wings.rect.move_ip(event.rel)
        nep_guns.rect.move_ip(event.rel)

    def nep_idle():
        nep_face.idle()
        nep_wings.idle()
        nep_guns.idle()

    def nep_flying():
        nep_face.flying()
        nep_wings.flying()
        nep_guns.flying()

    def idle_animation_update():
        idle_animation_body.update()
        idle_animation_wings.update()
        idle_animation_guns.update()
        idle_animation_face.update()

    def flying_animation_update():
        flying_animation_body.update()
        flying_animation_wings.update()
        flying_animation_guns.update()
        flying_animation_face.update()

    #Main While
    running = True
    moving = False

    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                AnimationSwitchInterval.stop()
                CloseEyesInterval.stop()
                OpenEyesInterval.stop()
                running = False

            elif event.type == USEREVENT+1: #Bonk Event
                nep_set_index()

            elif event.type == USEREVENT+2: #NoBonk Event
                nep_set_index()

            elif event.type == USEREVENT+3: #Border Event
                animation_state = IDLE
                nep_zero_index()

            elif event.type == USEREVENT+4: #Minus Event
                nep_minus_index()

            elif event.type == USEREVENT:
                if event.MyOwnType == ANIMATION_SWITCH:
                    if animation_state == IDLE:
                        animation_state = FLYING
                    elif animation_state == FLYING:
                        animation_state = IDLE
                elif event.MyOwnType == CLOSE_EYES_SWITCH:
                    nep_face.eyes_close()
                    OpenEyesInterval.start()
                elif event.MyOwnType == OPEN_EYES_SWITCH:
                    nep_face.eyes_open()
                    OpenEyesInterval.stop()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                AnimationSwitchInterval.stop()
                idle_animation_stop()
                if animation_state == FLYING:
                    nep_minus_index()
                if nep_face.rect.collidepoint(event.pos):
                    moving = True
                if nep_body.rect.collidepoint(event.pos):
                    moving = True
                if nep_wings.rect.collidepoint(event.pos):
                    moving = True
                if nep_guns.rect.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP and event.button == 1:
                if animation_state == FLYING:
                    nep_set_index()
                idle_animation_start()
                random_int = random.randint(rand_a, rand_b)
                AnimationSwitchInterval = set_nep_timer(AnimationSwitchEvent, random_int)
                moving = False

            elif event.type == MOUSEMOTION and moving:
                nep_rect_move()

        #Animation Switch
        if animation_state == IDLE:
            nep_idle()
            idle_animation_update()
        elif animation_state == FLYING:
            nep_flying()
            flying_animation_update()
            particle_y = nep_face.rect.y + 363 // 2
            particle_x = nep_face.rect.x + 200/scale #200
            particle_system.add_particle(particle_x, particle_y)

        particle_system.update()
        nep_group_fly.update()
        nep_group_main.update()
        screen.fill(t_color) #Transparent background
        clock.tick(FPS)
        particle_system.draw(screen)
        nep_group_fly.draw(screen)
        nep_group_main.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()