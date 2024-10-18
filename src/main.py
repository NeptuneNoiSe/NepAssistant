import pygame
import win32api
import win32con
import win32gui
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Neptune Assistant")
Icon = pygame.image.load('assets/icons/Chell_Logo.ico')
pygame.display.set_icon(Icon)
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))# , pygame.NOFRAME
done = False
#Colors
pantone = (74, 65, 42)  # Transparency color
dark_red = (139, 0, 0)
#windows on top
win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE |win32con.SWP_NOSIZE)
# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*pantone), 0, win32con.LWA_COLORKEY)

yuki = pygame.image.load('assets/images/work_in_progress.png')
img = pygame.transform.scale(yuki, (664, 578))
img.convert()
rect = img.get_rect()
rect.center = 1000, 500

running = True
moving = False
while running:

    for event in pygame.event.get():

        # Close if the user quits the
        # game
        if event.type == QUIT:
            running = False

        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        # Set moving as False if you want
        # to move the image only with the
        # mouse click
        # Set moving as True if you want
        # to move the image without the
        # mouse click
        elif event.type == MOUSEBUTTONUP:
            moving = False

        # Make your image move continuously
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(pantone)  # Transparent background
    screen.blit(img, rect)

    pygame.display.update()
