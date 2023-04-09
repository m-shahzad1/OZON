import pygame,importlib
import gameData as DB
importlib.reload(DB)
from pygame.locals import *
from gameObjects import GameObject
from pathlib import Path
import sys
import json
import math
import time,random
import threading
from runnables import home

class Map:
    def __init__(self,screen,enterLevel, enterHome,enterMaker):
        importlib.reload(DB)
        self.screen = screen
        self.enterlevel = enterLevel
        self.enterHome=enterHome
        self.enterMaker=enterMaker
        self.maxLevel = int(DB.map_unlock)
        print(self.maxLevel)
        self.player_level = [0, 0]
        self.player_pos =  [self.screen.get_width()//2, self.screen.get_height()//2]
        self.next_level = False
        self.enter_Level_trigger = False
        self.enter_npc_trigger = False
        self.can_move = False
        ##self.current_level = self.maxLevel
        self.enter_Hut_trigger=False
        self.enteredTime = pygame.time.get_ticks()
        self.setup()
        self.target_node_pos=[0,0]
        self.font = pygame.font.SysFont('Arial', 20, True, False)
 
       # position of nodes relative to center of the screen
        self.nodes = [
            {'name': 0, 'pos': [self.screen.get_width()*378/1000, self.screen.get_height()*402/600],'color':(255,255,255)},
            {'name': 1, 'pos': [self.screen.get_width()*258/1000, self.screen.get_height()*291/600],'color':(255,255,255)},
            {'name': 2, 'pos': [self.screen.get_width()*140/1000, self.screen.get_height()*123/600], 'color':(255,255,255)},
            {'name': 3, 'pos': [self.screen.get_width()*295/1000, self.screen.get_height()*29/600], 'color':(255,255,255)},
            {'name': 4, 'pos': [self.screen.get_width()*736/1000, self.screen.get_height()*90/600], 'color':(0,255,255)},
            {'name': 5, 'pos': [self.screen.get_width()*844/1000, self.screen.get_height()*170/600],'color':(255,255,255)},
            {'name': 6, 'pos': [self.screen.get_width()*680/1000, self.screen.get_height()*203/600], 'color':(255,255,255)},
            {'name': 7, 'pos': [self.screen.get_width()*783/1000, self.screen.get_height()*320/600], 'color':(255,255,255)},
        ]

        self.huts=[
             {'name': 'Hut 1', 'pos': [self.screen.get_width()*332/1000, self.screen.get_height()*300/600]},
            {'name': 'Hut 2', 'pos': [self.screen.get_width()*636/1000, self.screen.get_height()*161/600]},
            {'name': 'makerHut', 'pos': [self.screen.get_width()*757/1000, self.screen.get_height()*441/600]}
        ]

        self.npcs=[
             {'name': 'npc1','pos': [self.screen.get_width()*1/2, self.screen.get_height()*1/5],'angle': 0, 'speed': 7,'radius': 75,'img': Path(r'Code/sprites/map/npc1.png') },
             {'name': 'npc2', 'pos': [self.screen.get_width()*1/2, self.screen.get_height()*1/2], 'angle': math.pi, 'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc2.png')},
             {'name': 'npc3', 'pos': [self.screen.get_width()*1/2, self.screen.get_height()*8/10], 'angle': 45,'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc3.png') },
             {'name': 'npc4', 'pos': [self.screen.get_width()*1/3, self.screen.get_height()*8/10], 'angle': 35,'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc4.png') },
             {'name': 'npc5', 'pos': [self.screen.get_width()*1/4, self.screen.get_height()*4/5], 'angle': 80,'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc5.png') },
             {'name': 'npc6', 'pos': [self.screen.get_width(), self.screen.get_height()], 'angle': 55,'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc1.png')},
             {'name': 'npc7', 'pos': [self.screen.get_width()*5/6, self.screen.get_height()*8/10], 'angle': 70,'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc1.png') },
             {'name': 'npc8', 'pos': [self.screen.get_width()*6/7, self.screen.get_height()*8/10], 'angle': 35,'speed': 7,'radius': 75, 'img': Path(r'Code/sprites/map/npc1.png') }
        ]

    def setup(self):
        importlib.reload(DB)
        self.map_img = GameObject(self.screen,self.screen.get_rect(),DB.maps[self.maxLevel]['background'])


    def randomInteraction(self):
        ##time.sleep(30
        currentTime  = pygame.time.get_ticks()
        #delay = random.uniform(0, 10)  # random delay between 0 and 10 seconds
        #time.sleep(delay)
        enterTime = int(self.enteredTime)
        if (currentTime-enterTime)>30000000:
            if random.random() < 0.2:  # 20% chance
                self.enterlevel(3)

    # WHILE LOOP
    def run(self):
        self.input()
        self.show()
        self.update()
        # self.overWorld()
    
    def updateNodes(self):
        for node in self.nodes:
            if  node['name']==self.maxLevel: 
                node['color'] = 'red'
            if node['name'] < self.maxLevel:
                node['color'] = 'green'
            if node['name'] > self.maxLevel:
                node['color'] = 'grey'

    def input(self):
        # Change this logic, this is just for testing
        keys = pygame.key.get_pressed()
        mpos = pygame.mouse.get_pos()
        mpress = pygame.mouse.get_pressed()
        if mpress[0] == True: 
            pass
             #print(mpos[0],mpos[1])

        if keys[pygame.K_w]:
            if self.player_pos[1] > 0:
                self.player_pos[1] -= 16
        if keys[pygame.K_s]:
             if self.player_pos[1] < self.screen.get_height():
                self.player_pos[1] += 16
        if keys[pygame.K_a]:
            if self.player_pos[0] > 0:
                self.player_pos[0] -= 17
        if keys[pygame.K_d]:
             if self.player_pos[0] < self.screen.get_width():
                self.player_pos[0] += 17

        # Check if player is near a level node
        for node in self.nodes:
            #checks distance between player's position and level node position 
            distance = math.sqrt((self.player_pos[0] - node['pos'][0]) ** 2 + (self.player_pos[1] - node['pos'][1]) ** 2)
            if distance <= 20:  # Change 20 to adjust the trigger distance
                self.enter_Level_trigger = True
                self.current_level_name = node['name']
                interact_text = self.font.render(f"Press T to interact with {node['name']}", True, (255, 255, 255))
                interact_rect = interact_text.get_rect(center=(node['pos'][0], node['pos'][1] - 40))
                self.screen.blit(interact_text, interact_rect)
                break
            else:
                self.enter_Level_trigger = False

                # Enter level logic

        if self.enter_Level_trigger and keys[pygame.K_SPACE]:
            if self.current_level_name == 0:
                self.enterlevel(0)
            if self.current_level_name == 1 and self.maxLevel >= 1:
                self.enterlevel(1)
            if self.current_level_name == 2 and self.maxLevel >= 2:
                self.enterlevel(2)
            if self.current_level_name == 3 and self.maxLevel >= 3:
                self.enterlevel(3)
            if self.current_level_name == 4 and self.maxLevel >= 4:
                self.enterlevel(4)
            if self.current_level_name == 5 and self.maxLevel >= 5:
                self.enterlevel(5)
            if self.current_level_name == 6 and self.maxLevel >= 6:
                self.enterlevel(6)
            if self.current_level_name == 7 and self.maxLevel >= 7 and DB.makerLevel['boss']!=['']:
                 self.enterlevel(7)
        print(DB.makerLevel['boss'])    
        for hut in self.huts:
            #checks distance between player's position and level node position 
            distance = math.sqrt((self.player_pos[0] - hut['pos'][0]) ** 2 + (self.player_pos[1] - hut['pos'][1]) ** 2)
            if distance <= 50:  # Change 20 to adjust the trigger distance
                self.enter_Hut_trigger = True
                interact_text1 = self.font.render(f"Press T to interact with Hut", True, (255, 255, 255))
                interact_rect1 = interact_text1.get_rect(center=(hut['pos'][0], hut['pos'][1] - 40))
                self.screen.blit(interact_text1, interact_rect1)
                break
            else:
                self.enter_Hut_trigger = False
        
        if self.enter_Hut_trigger and keys[pygame.K_SPACE]:
                if hut['name'] == 'makerHut':
                    if self.maxLevel ==7:
                        self.enterMaker()
                else:
                    self.enterHome()
        
    def update(self):
        self.updateNodes()
        #self.updateplayerposition()
        pygame.display.flip()
        
    def show(self):
        # print(self.maxLevel)
        self.randomInteraction()
        self.map_img.show()
        self.map_img = self.map_img = GameObject(self.screen,self.screen.get_rect(),DB.maps[self.maxLevel]['background'])

        # SHOW NODES
        for node in self.nodes:
            pygame.draw.circle(self.screen, node['color'], node['pos'], 27)
            if node['name'] == 7:
                pygame.draw.circle(self.screen, node['color'], node['pos'], 27)
                text = self.font.render('M', True, (0, 0, 0))
                text_rect = text.get_rect(center=node['pos'])
                self.screen.blit(text, text_rect)
            else:
                #Render node's name as text
                text = self.font.render(str(node['name']), True, (0, 0, 0))
                # Gets rectangle for the text surface and centers it at the node's position
                text_rect = text.get_rect(center=node['pos'])
                # Draw the text on the screen at text rectangle's position
                self.screen.blit(text, text_rect)
                # print(self.maxLevel)
        #SHOW HUTS
        for hut in self.huts:
            if hut['name'] == 'makerHut':
                hut_image = pygame.image.load(Path('Code/sprites/map/makerhut.png'))
                hut_image = pygame.transform.scale(hut_image, (100, 100))

            else:
                hut_image = pygame.image.load(Path('Code/sprites/map/homemap.png'))
                hut_image = pygame.transform.scale(hut_image, (50, 50))

            # Get the rectangle for the image and center it at the hut's position
            hut_rect = hut_image.get_rect(center=hut['pos'])
            # Draw the image
            self.screen.blit(hut_image, hut_rect)
            text = self.font.render(hut['name'], True, (0, 0, 0))
            text_rect = text.get_rect(center=hut['pos'])  

            player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], 32, 32)
            if hut_rect.colliderect(player_rect):
                # Display interaction message and wait for T key press
                interact_text1 = self.font.render(f"Press Space to enter Hut", True, (255, 255, 255))
                interact_rect1 = interact_text1.get_rect(center=(hut['pos'][0], hut['pos'][1] - 40))
                self.screen.blit(interact_text1, interact_rect1)
         # SHOW NPCS
        # for npc in self.npcs:
        #     if not self.can_move:
        #     # Update angle randomly
        #         npc['angle'] += random.uniform(-0.1, 0.1)

        #         # Calculate new position based on angle and speed
        #         npc['pos'][0] += int(npc['speed'] * math.cos(npc['angle']))
        #         npc['pos'][1] += int(npc['speed'] * math.sin(npc['angle']))

        #         # Wrap around the screen if NPC goes out of bounds
        #         if npc['pos'][0] < 0:
        #             npc['pos'][0] = self.screen.get_width()
        #         elif npc['pos'][0] > self.screen.get_width():
        #             npc['pos'][0] = 0
        #         if npc['pos'][1] < 0:
        #             npc['pos'][1] = self.screen.get_height()
        #         elif npc['pos'][1] > self.screen.get_height():
        #             npc['pos'][1] = 0

        #     # Draw the NPC on the screen
        #     #npc_img = pygame.image.load('Code\sprites\map\hut.jpg')
        #     npc_img = pygame.image.load(Path('Code/sprites/map//npc.png'))
        #     npc_img = pygame.transform.scale(npc_img, (50, 50))

            
        #     npc_rect = npc_img.get_rect(center=npc['pos'])
        #     self.screen.blit(npc_img, npc_rect)

        #     #npc img upon T display
        #     npc_t_img = pygame.image.load(npc['img'])
        #     npc_t_img = pygame.transform.scale(npc_t_img, (250, 250))

        #     # Check if player is close enough to interact with NPC
        #     player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], 32, 32)
        #     if npc_rect.colliderect(player_rect):
        #         # Display interaction message and wait for T key press
        #         interact_text = self.font.render(f"Press T to interact with {npc['name']}", True, (255, 255, 255))
        #         interact_rect = interact_text.get_rect(center=(npc['pos'][0], npc['pos'][1] - 40))
        #         self.screen.blit(interact_text, interact_rect)
        #         keys = pygame.key.get_pressed()
        #         if keys[pygame.K_t]:
        #             self.can_move = True
        #             text = self.font.render("Hello, I am " + npc['name'], True, (255, 255, 255))
        #             #self.screen.blit(text, (npc['pos'][0] + 10, npc['pos'][1] - 20))
        #             self.screen.blit(npc_t_img, (npc['pos'][0] + 10, npc['pos'][1] - 20))
        #         else:
        #             self.can_move = False
        # Load NPC image and scale it outside of the loop
        npc_img = pygame.image.load(Path('Code/sprites/map//npc.png'))
        npc_img = pygame.transform.scale(npc_img, (50, 50))

        for npc in self.npcs:
            if not self.can_move:
          # Update angle randomly
                npc['angle'] += random.uniform(-0.1, 0.1)

        # Calculate new position based on angle and speed
                npc['pos'][0] += int(npc['speed'] * math.cos(npc['angle']))
                npc['pos'][1] += int(npc['speed'] * math.sin(npc['angle']))

                # Wrap around the screen if NPC goes out of bounds
                if npc['pos'][0] < 0:
                    npc['pos'][0] = self.screen.get_width()
                elif npc['pos'][0] > self.screen.get_width():
                    npc['pos'][0] = 0
                if npc['pos'][1] < 0:
                    npc['pos'][1] = self.screen.get_height()
                elif npc['pos'][1] > self.screen.get_height():
                    npc['pos'][1] = 0

        # Draw the NPC on the screen
            npc_rect = npc_img.get_rect(center=npc['pos'])
            self.screen.blit(npc_img, npc_rect)

            # Check if player is close enough to interact with NPC
            player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], 32, 32)
            if npc_rect.colliderect(player_rect):
                # Display interaction message and wait for T key press
                interact_text = self.font.render(f"Press T to interact with {npc['name']}", True, (255, 255, 255))
                interact_rect = interact_text.get_rect(center=(npc['pos'][0], npc['pos'][1] - 40))
                self.screen.blit(interact_text, interact_rect)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_t]:
                    self.can_move = True
                    # Load and draw NPC image upon T key press
                    npc_t_img = pygame.image.load(npc['img'])   
                    npc_t_img = pygame.transform.scale(npc_t_img, (250, 250))
                    text = self.font.render("Hello, I am " + npc['name'], True, (255, 255, 255))
                    #self.screen.blit(npc_t_img, (npc['pos'][0] + 10, npc['pos'][1] - 20))
                    self.screen.blit(npc_t_img, (max(0, npc['pos'][0] - 110), max(0, npc['pos'][1] - 280)))
                else:
                    self.can_move = False
            # Show the player icon
        pygame.draw.circle(self.screen, (13,1,226), self.player_pos, 10)