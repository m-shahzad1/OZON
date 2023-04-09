import pygame
import sys
#import data.Engine as e
from pygame.locals import *
import json
from pathlib import Path


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20, True, False)

clock = pygame.time.Clock()


WINDOWN_SIZE = (960, 540)
screen = pygame.display.set_mode(WINDOWN_SIZE)

overWorld = pygame.image.load(Path('Code/sprites/map/mapLevel0passed.png'))
overWorld = pygame.transform.smoothscale(overWorld, WINDOWN_SIZE)

data = {}

c_m = -1
c_s = -1

step = 60
sub_step = -1
sub_step_raw = -1
moving = [0, 0]

prev_level = -1
player_level = [-1. -1]
player_pos = [-1, -1]

c_l = False
c_r = False
next = [0,0]
end_animation = False
while True:
    
    screen.fill([0,0,0])
    mx, my = pygame.mouse.get_pos()
    
    screen.blit(overWorld, [WINDOWN_SIZE[0] / 2 - overWorld.get_width() / 2, WINDOWN_SIZE[1] / 2 - overWorld.get_height() / 2])

    if end_animation:
        end_animation = False
    
    T_mouse_pos = font.render(f"X: {mx} | Y: {my}", True, [255, 255, 255])
    Level = font.render(f"LEVEL: {player_level[0]}", True, [255, 255, 255])
    
    if c_l:
        if player_pos == [-1, -1]:
            player_pos = [mx, my]
            player_level = [0, 0]
        
        c_m += 1
        c_s = 0
        data[c_m] = {}
        data[c_m][c_s] = [mx, my]
        #print(data)
    if c_r:
        c_s += 1
        data[c_m][c_s] = [mx, my]
        #print(data)
    
    # print(data)
    for m_num, se_path in data.items():
        for s_num, m_pos in se_path.items():
            if s_num == 0:
                pygame.draw.circle(screen, [255,0,0], m_pos, 10)
            else:
                pygame.draw.circle(screen, [0,0,255], m_pos, 5)
    
    
    if player_level[0] != -1:
        pygame.draw.rect(screen, [255, 0, 255], 
                        [player_pos[0] - 15, 
                        player_pos[1] - 15, 
                        30, 30])
    
    if next[0] == 1:
        
        prev_level = player_level[0]
        player_level[0] += next[1]
        
        if player_level[0] < 0:
            player_level[0] = 0
        elif player_level[0] > c_m:
            player_level[0] = c_m
        
        if next[1] == -1:
            player_level[1] = len(data[player_level[0]])
        
        next[0] = 2

        if prev_level == player_level[0]:
            next = [0, 0]
            player_level[1] = 0
        else:
            if next[1] == 1:
                sub_step_raw = step // len(data[player_level[0] - 1])
            else:
                sub_step_raw = step // len(data[player_level[0]])

        sub_step = sub_step_raw
        
    if next[0] == 2:
        player_level[1] += next[1]
        if player_level[1] == len(data[prev_level]) and next[1] == 1:
            vec_x = (data[player_level[0]][0][0] - player_pos[0]) / sub_step
            vec_y = (data[player_level[0]][0][1] - player_pos[1]) / sub_step
        elif player_level[1] == len(data[player_level[0]]) and next[1] == -1:
            vec_x = (data[player_level[0]][len(data[player_level[0]]) - 1][0] - player_pos[0]) / sub_step
            vec_y = (data[player_level[0]][len(data[player_level[0]]) - 1][1] - player_pos[1]) / sub_step
        else:
            if next[1] == 1:
                vec_x = (data[prev_level][player_level[1]][0] - player_pos[0]) / sub_step
                vec_y = (data[prev_level][player_level[1]][1] - player_pos[1]) / sub_step
            else:
                vec_x = (data[player_level[0]][player_level[1]][0] - player_pos[0]) / sub_step
                vec_y = (data[player_level[0]][player_level[1]][1] - player_pos[1]) / sub_step

        # print(player_level)
        moving = [vec_x, vec_y]
        next[0] = 3
    
    if next[0] == 3:
        player_pos[0] += moving[0]
        player_pos[1] += moving[1]
        
        sub_step -= 1
        if sub_step == 0:
            sub_step = sub_step_raw
            next[0] = 2
            
            if (player_level[1] == len(data[prev_level]) and next[1] == 1) or player_level[1] == 0:
                next = [0, 0]
                player_level[1] = 0
                end_animation = True

    c_l = False
    c_r = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                c_l = True
            elif event.button == 3:
                c_r = True
        elif event.type == KEYDOWN:
            if event.key == K_d:
                next = [1,1]
            elif event.key == K_a:
                next = [1,-1]
            elif event.key == K_s:
                with open("path_overworld.json", "w") as f:
                    json.dump(data, f)
    
    clock.tick(60)
    
    screen.blit(T_mouse_pos, [0,0])
    screen.blit(Level, [0,20])
    pygame.display.update()