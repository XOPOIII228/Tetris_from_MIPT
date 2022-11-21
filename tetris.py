import pygame
import random, time, sys
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load("zvuk-tetrisa-na-konsoli.mp3")
pygame.mixer.music.play()

fps = 30
window_w, window_h = 800, 600       
block = 20      
field_w = 20    
field_h = 25    
side_move_time, down_move_time = 0.1, 0.1 
game_screen_Hpos = int((window_w -field_w*block)/2)  
game_screen_Vpos = window_h - (field_h * block) 
colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))
lightcolors = ((30, 30, 255), (50, 255, 50), (255, 30, 30), (255, 255, 30))         
white, gray, black  = (255, 255, 255), (185, 185, 185), (0, 0, 0)
board_color, background_color, txt_color, title_color, info_color = white, black, white, colors[3], colors[2]

figure_w, figure_h = 5, 5      
empty = 'o'
figures = {'S': [['ooooo',
                  'ooooo',
                  'ooxxo',
                  'oxxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'oooxo',
                  'ooooo']],
           'Z': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'oxooo',
                  'ooooo']],
           'L': [['ooooo',
                  'oxooo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxxo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oooxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'oxxoo',
                  'ooooo']],
           'J': [['ooooo',
                  'oooxo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oxooo',
                  'ooooo'],
                 ['ooooo',
                  'oxxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo']],
           'I': [['ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'xxxxo',
                  'ooooo',
                  'ooooo']],
           'O': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'oxxoo',
                  'ooooo']],
           'T': [['ooooo',
                  'ooxoo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'ooxoo',
                  'ooooo']]}

def pauseScreen():
        pause = pygame.Surface(( 800, 600))  
        pause.set_alpha(150) 
        pause.fill(( 128 , 128,128))               
        display.blit(pause, (0, 0))

def main():
    global fps_clock, display, basic_font, big_font
    pygame.init()
    fps_clock = pygame.time.Clock() 
    display = pygame.display.set_mode((window_w, window_h)) 
    basic_font = pygame.font.SysFont('arial', 20) 
    big_font = pygame.font.SysFont('arial', 45) 
    pygame.display.set_caption('Тетрис') 
    showText('Тетрис') 
    while True: 
        runTetris() 
        pauseScreen()
        showText('Конец игры') 
print('миша молодец')
