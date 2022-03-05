from shutil import move
from tkinter.messagebox import YES
from turtle import Screen
import pygame
from constants import *
from board import *
from characters import *
game_phase = 0
selected_character = pygame.sprite.GroupSingle()
characters_on_board = pygame.sprite.Group()
team_one = pygame.sprite.Group()
team_two = pygame.sprite.Group()
turn = True
is_selected = False
dragging = False


def update():
    global selected_character, characters_on_board
    SCREEN.fill(BLACK)
    draw_board()
    draw_character_slots()
    pygame.sprite.Group.draw(characters_on_board, SCREEN)

def select_character(clickX, clickY):
    global is_selected, characters_on_board, team_one, team_two, selected_character
    if game_phase == 0:
        if is_selected == False:
            for character in all_characters:
                if character.rect.collidepoint(clickX, clickY):
                    selected_character.add(character)
                    all_characters.remove(character)
                    is_selected = True
        
            for characters in characters_on_board:
                if characters.rect.collidepoint(clickX, clickY):
                    selected_character.add(characters)
                    all_characters.remove(characters)
                    characters_on_board.remove(characters)
                    is_selected = True
                    clickX, clickY = 0, 0


def drag_character(clickX, clickY):
    global is_selected, selected_character, characters_on_board, dragging
    if game_phase == 0 or 1:
        if is_selected == True:
            for character in selected_character:
                dragging = True
                x, y = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                mouse_rect.center = (x, y)
                setattr(character, "rect", mouse_rect)
                SCREEN.fill(BLACK)
                draw_board()
                pygame.draw.rect(SCREEN, RED, trash_bin())
                characters_on_board.draw(SCREEN)
                selected_character.draw(SCREEN)
                if trash_bin().collidepoint(clickX, clickY):
                    for character in selected_character:
                        all_characters.add(character)
                        characters_on_board.remove(character)
                        is_selected = False
                        dragging = False
                        SCREEN.fill(BLACK)
                        draw_board()
                        draw_character_slots()
                        characters_on_board.draw(SCREEN)
            if dragging == True:
                place_character(clickX, clickY)
def place_character(clickX, clickY):
    pass
            

def sum_levels():
    levels = 0
    for character in characters_on_board:
        levels += character.level
    return levels

def new_phase():
    global game_phase
    game_phase += 1
    draw_phase()

def draw_phase():
    if game_phase == 1:
        characters_on_board.clear(SCREEN, SCREEN)
        all_characters.clear(SCREEN, SCREEN)
        all_characters.add(all_characters_list)
        draw_board()
        draw_character_slots()