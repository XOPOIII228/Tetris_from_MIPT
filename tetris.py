import pygame
import random, time, sys
from pygame.locals import *

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
