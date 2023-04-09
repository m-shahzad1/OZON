import pygame,time,importlib
import gameData
importlib.reload(gameData)
# from gameData import home,map_unlock,players
from gameObjects import GameObject
from pathlib import Path
from runnables import level,maker,map,sequences


class Home():
    def __init__(self,screen,enterMap):
        importlib.reload(gameData)
        from gameData import home,map_unlock as m,players
        self.home = home
        self.m = m
        self.unlock = players['attackUnlock']
        self.sel = players['selected']
        self.enter_map = enterMap
        self.screen = screen
        self.backgroundImg = GameObject(screen,screen.get_rect(),home[self.sel])
        
    def input(self):
        mpos = pygame.mouse.get_pos()
        mpress = pygame.mouse.get_pressed()

        ##Setting up the rectangles for the colour selection buttons
        #rect3 = pygame.Rect(180,340,129,200) #Green
        screenWidth = self.screen.get_width()
        screenHeight = self.screen.get_height()
        rect = pygame.Rect(screenWidth*(0.850),screenHeight*(518/600),screenWidth*(0.130),screenHeight*(45/600)) #Button to Map
        rect2 = pygame.Rect(screenWidth*(0.710),screenHeight*(518/600),screenWidth*(0.130),screenHeight*(45/600))# Button for New Colour
        rect3 = pygame.Rect(screenWidth*(0.180),screenHeight*(0.56),screenWidth*(0.129),screenHeight*(1/3))#Green character 
        rect4 = pygame.Rect(screenWidth*(0.450),screenHeight*(0.56),screenWidth*(0.129),screenHeight*(1/3)) #Blue character
        rect5 = pygame.Rect(screenWidth*(0.680),screenHeight*(0.56),screenWidth*(0.129),screenHeight*(0.30)) #Red Character
        #(left,top,width,height)

        if rect.collidepoint(pygame.mouse.get_pos()):
            if mpress[0] == True:
                importlib.reload(map)
                importlib.reload(level)
                importlib.reload(sequences)
                importlib.reload(maker)
                
                self.enter_map()

        elif rect2.collidepoint(pygame.mouse.get_pos()):
            if mpress[0] == True:
                msg = self.sel+' '+ self.m + ' '+self.unlock
                f = open(Path(r'Code/data/master.txt'),'w')
                f.write(msg)

        if rect3.collidepoint(pygame.mouse.get_pos()):
            if mpress[0] == True:
                self.backgroundImg = GameObject(self.screen,self.screen.get_rect(),self.home['green'])
                self.sel = 'green'
        elif rect4.collidepoint(pygame.mouse.get_pos()):
            if mpress[0] == True:
                self.backgroundImg = GameObject(self.screen,self.screen.get_rect(),self.home['blue'])
                self.sel = 'blue'
        
        elif rect5.collidepoint(pygame.mouse.get_pos()):
            if mpress[0] == True:
                self.backgroundImg = GameObject(self.screen,self.screen.get_rect(),self.home['red'])
                self.sel = 'red'

    def run(self):
        self.input()
        self.show()

    def show(self):
        self.backgroundImg.show()
        

    