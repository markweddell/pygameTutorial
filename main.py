import pygame

from PIL import Image
import requests
from io import BytesIO


#Initalize Pygame
pygame.init()
size = width, height = 320, 240
title = "First app"


image = 'icon.png'


bg = 36, 36, 36
speed = [0, 0]

#Create Window with custom title
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)
icon = pygame.image.load(image)
iconr = icon.get_rect()

#Main loop
run = True
while run:
    
    #Change direction if it reaches the borders
    if iconr.left<0 or iconr.right>width:
        speed[0] = -10
    if iconr.top<0 or iconr.bottom>height:
        speed[1] = -10
    
    #Exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False;
        if event.type == pygame.KEYDOWN:
            if event.key == 275: #RIGHT
                speed[0] = 10
            if event.key == 276: #LEFT
                speed[0] = -10
            if event.key == 273: #UP
                speed[1] = -10
            if event.key == 274: #DOWN
                speed[1] = 10
    
    #Move the icon
    iconr = iconr.move(speed)
    speed = [0, 0]

    window.fill(bg)
    window.blit(icon, iconr)
    pygame.display.flip()
