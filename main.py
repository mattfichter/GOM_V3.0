import pygame
from constants import *
from board import *
from characters import *
from game import *
from button import *

clickX, clickY = 0, 0

def main():
    pygame.init()
    run = True
    SCREEN 
    draw_board()
    draw_character_slots()
  
    while run:
        global clickX, clickY, dragging
        drag_character(clickX, clickY)
        if sum_levels() == 10:
            Button(BUTTON, ready_button_rect, 'Ready').draw(SCREEN)
        if ready_button_rect.collidepoint(clickX, clickY):
            new_phase()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                clickX, clickY = event.pos
                select_character(clickX, clickY)
                  
            if event.type == pygame.MOUSEMOTION:
                motionX, motionY = event.pos

        pygame.display.update()

main()