from constants import *
from characters import *

board_rect_list = [[[] for i in range(6)] for i in range(6)]
board = [[[] for i in range(6)] for i in range(6)]
character_slots = []

def draw_board():
    global board_rect_list
    x, y =  BOARDSTART
    for row in range(ROWS):
        for col in range(COLS):
            if row % 2 == 0 and col % 2 == 0 or row % 2 == 1 and col % 2 == 1:
                board_rect_list[col][row] = []
                board_rect_list[col][row].append(pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(SCREEN, GREY, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                x += SQUARE_SIZE
            else:
                board_rect_list[col][row] = []
                board_rect_list[col][row].append(pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(SCREEN, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                x += SQUARE_SIZE
            if x >= BOARDEND[0]:
                x = BOARDSTART[0] 
                y += SQUARE_SIZE

def draw_character_slots():
    global character_slots, all_characters, all_characters_list
    x, y = CHARACTERSTART
    character_slots.clear()
    for characters in all_characters_list:
        character_slot_rect = pygame.Rect((x, y), (SQUARE_SIZE, SQUARE_SIZE))
        character_slots.append(character_slot_rect)
        x += SQUARE_SIZE
    for character in all_characters:
        setattr(character, "rect", character_slots[character.index])
        SCREEN.blit(character.image, character.rect)

def trash_bin():
    trash_rect = pygame.Rect(WIDTH/1.2, HEIGHT/1.2, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(SCREEN, RED, (trash_rect))
    return trash_rect