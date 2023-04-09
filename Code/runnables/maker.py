import pygame,time,importlib
import gameData
importlib.reload(gameData)
from gameData import res,maker_sprites,levels
from block import Platform
from gameData import levels
from gameObjects import GameObject
from enemy import Enemy
from berry import Berry
from player import Player
from boss import Boss
from pathlib import Path
import runnables.map,runnables.level

class Maker:
    def __init__(self,screen,level,enterMap):
        # Level to be created:
        self.level = levels[level]

        # Screen
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Display Window (Portion of level shown)
        self.top_bar = (self.screen_rect.w,self.screen_rect.h/8)
        self.display_cords = (0,self.top_bar[1])
        self.display_rect = pygame.Rect(self.display_cords[0],self.display_cords[1],self.screen_rect.w-self.top_bar[1],self.screen_rect.h-self.top_bar[1])
        self.display_surface = pygame.Surface((self.display_rect.w,self.display_rect.h)).convert()

        # Mouse Stuff
        self.mousePressed = False

        # Level Surface (Actual Level)
        self.xStretch = self.level['stretch']
        self.level_size = ((self.display_rect.w)*self.xStretch,self.display_rect.h)
        self.maker_screen = pygame.Surface(self.level_size)
        self.maker_screen.fill('violet')
        self.maker_screen.set_colorkey('violet')
        self.maker_screen_rect = self.maker_screen.get_rect()

        # Increments for Lines
        self.yinc = self.display_rect.h/res[1]
        self.xinc = self.display_rect.w/res[0]

        self.topBarSetup()
        self.sideBarSetup('')

        # Level Stuff
        self.level = levels[0]
        self.platforms = []
        self.enemies = []
        self.berries = []
        self.player = Player(self.display_surface,self.display_rect,(3,3),'blue',2)
        self.boss = None
        self.item=None

        # Scrolling Stuff
        self.lateral = 0

        # Enter Map Again
        self.enterMap = enterMap

        backRect = self.display_rect.copy()
        backRect.w=backRect.w*1.4
        self.background = GameObject(self.screen,backRect,maker_sprites['backgrounds']['night'])
        # self.background.rect.w = self.background.rect.w*1.5

    def topBarSetup(self):
        topBarLocs = [pygame.Rect(self.top_bar[0]*(0.015+0.2*i),self.top_bar[1]*0.15,self.top_bar[0]*0.15,self.top_bar[1]*0.75) for i in range(5)]
        self.top_bar_btns = [(GameObject(self.screen,topBarLocs[i],s)) for s,i in zip(maker_sprites['top_bar'].values(),range(len(maker_sprites['top_bar'].values())))]
    
    def sideBarSetup(self,index):
        self.topSel = index
        self.sideSel=0
        if index=="":
            self.side_bar_btns = []
            return
        num = len(maker_sprites['side_bar'][index].values())
        sideBarLocs = [pygame.Rect(self.display_rect.w+self.top_bar[1]/4,self.top_bar[1]*1.15*(i+1),self.top_bar[1]*0.5,self.top_bar[1]*0.5) for i in range(num)]
        self.side_bar_btns = [(GameObject(self.screen,sideBarLocs[i],s)) for s,i in zip(maker_sprites['side_bar'][index].values(),range(num))]
        self.item = self.side_bar_btns[0]

    def input(self):
        self.mouseInput()
        self.keyInput()
    
    def keyInput(self):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_RETURN]:
            # This will have to change depending on which level we want to enter
            self.enterMap()
            return
        if keys[pygame.K_d] and self.lateral+self.xinc<self.maker_screen_rect.w-self.display_rect.w:
            self.lateral+=self.xinc
        if keys[pygame.K_a] and self.lateral-self.xinc>=0:
            self.lateral-=self.xinc

    def mouseInput(self):
        # FOR TOP BAR
        self.topBarMouseCheck()
        self.sideMouseCheck()

        self.mousePlacer()

    def mousePlacer(self):
        if self.item==None:
            return
        if self.topSel=='platforms':
            if pygame.mouse.get_pressed()[0]==1 and self.mousePressed == False:
                self.platform_cords = self.indexMouse(pygame.mouse.get_pos())
                if self.platform_cords is None:
                    return
                self.mousePressed = True
            elif pygame.mouse.get_pressed()[0]==0 and self.mousePressed == True:
                self.mousePressed = False
                mPos = self.indexMouse(pygame.mouse.get_pos())
                if mPos is None:
                    return
                self.placePlatform(mPos)
        elif self.topSel=='enemies':
            if pygame.mouse.get_pressed()[0]==1:
                mPos = self.indexMouse(pygame.mouse.get_pos())
                if mPos is None:
                    return
                self.placeEnemy(mPos)
        elif self.topSel=='berries':
            if pygame.mouse.get_pressed()[0]==1:
                mPos = self.indexMouse(pygame.mouse.get_pos())
                if mPos is None:
                    return
                self.placeBerry(mPos)
        elif self.topSel=='bosses':
            if pygame.mouse.get_pressed()[0]==1:
                mPos = self.indexMouse(pygame.mouse.get_pos())
                if mPos is None:
                    return
                self.placeBoss(mPos)

    def topBarMouseCheck(self):
        if pygame.mouse.get_pressed()[0]==1 and self.mousePressed==False and self.top_bar_btns[0].rect.collidepoint(pygame.mouse.get_pos()) and self.boss != None:
            self.save()
            self.enterMap()
        elif pygame.mouse.get_pressed()[0]==1 and self.mousePressed==False and self.top_bar_btns[1].rect.collidepoint(pygame.mouse.get_pos()):
            if self.topSel=='platforms':
                self.sideBarSetup("")
            else:
                self.sideBarSetup('platforms')
            time.sleep(0.5)
        elif pygame.mouse.get_pressed()[0]==1 and self.mousePressed==False and self.top_bar_btns[2].rect.collidepoint(pygame.mouse.get_pos()):
            if self.topSel=='berries':
                self.sideBarSetup("")
            else:
                self.sideBarSetup('berries')
            time.sleep(0.5)
        elif pygame.mouse.get_pressed()[0]==1 and self.mousePressed==False and self.top_bar_btns[3].rect.collidepoint(pygame.mouse.get_pos()):
            if self.topSel=='enemies':
                self.sideBarSetup("")
            else:
                self.sideBarSetup('enemies')
            time.sleep(0.5)
        elif pygame.mouse.get_pressed()[0]==1 and self.mousePressed==False and self.top_bar_btns[4].rect.collidepoint(pygame.mouse.get_pos()):
            if self.topSel=='bosses':
                self.sideBarSetup("")
            else:
                self.sideBarSetup('bosses')
            time.sleep(0.5)

    def sideMouseCheck(self):
        for btn,i in zip(self.side_bar_btns,range(100)):
            if pygame.mouse.get_pressed()[0]==1 and self.mousePressed==False and btn.rect.collidepoint(pygame.mouse.get_pos()):
                self.sideSel = i
                # This changes what 'mode' maker is in
                self.item = self.side_bar_btns[i]
                return
        
    def placePlatform(self,mPos):
        xc = (self.platform_cords[0],mPos[0])
        yc = (self.platform_cords[1],mPos[1])
        cords = [min(xc),min(yc),max(xc),max(yc)]
        type = self.sideSel
        if type==0:
            type = 'grass'
        elif type==1:
            type = 'stone'
        elif type==2:
            type = 'poison'
        elif type == 3:
            type = 'brown'
        p = maker_sprites['side_bar']['platforms'][type]
        self.platforms.append(Platform(self.display_surface,self.display_rect,(cords[0],cords[1],cords[2],cords[3],'normal',p)))

    def placeEnemy(self,mPos):
        if self.sideSel==0:
            type = 'enemyMove'
        else:
            type = 'enemyStill'
        self.enemies.append(Enemy(self.display_surface,self.display_rect,[mPos[0],mPos[1],type]))
        time.sleep(0.5)
        return
    
    def placeBerry(self,mPos):
        if self.sideSel==0:
            type = 'full'
        else:
            type = 'part'
        b = maker_sprites['side_bar']['berries'][type]
        self.berries.append(Berry(self.display_surface,self.display_rect,(mPos[0],mPos[1],type,b)))
        time.sleep(0.5)
        return
    
    def placeBoss(self,mPos):
        if self.sideSel==0:
            type = 'b1'
        else:
            type = 'b2'
        b = maker_sprites['side_bar']['bosses'][type]
        self.boss = (Boss(self.display_surface,self.display_rect,(mPos[0],mPos[1],self.sideSel)))
        time.sleep(0.5)
        return

    def indexMouse(self,mPos):
        # mPos[0]+=self.display_rect.x
        # mPos[1]+=self.display_rect.y
        if(mPos[1]<self.top_bar[1] or mPos[0]>self.display_rect.w):
            return None
        mPos = (mPos[0]+self.lateral,self.screen_rect.h-mPos[1])
        for i in range (res[0]*self.xStretch-1,-1,-1):
            if mPos[0] >= i*self.xinc:
                for e in range (res[1]-1,-1,-1):
                    if mPos[1] >= e*self.yinc:
                        return (i,e)
        return None

    def show(self):
        # Reset Screen
        self.maker_screen.fill('violet')

        # BACKGROUND CAMERA
        cam = pygame.Rect((self.background.rect.w-self.display_rect.w)*((self.display_rect.w+self.lateral)/self.maker_screen_rect.w),0,self.screen_rect.w-self.display_cords[1],self.maker_screen_rect.h)
        self.screen.blit(self.background.image,self.display_cords,cam)

        self.showMenus()

        # Grid System
        [pygame.draw.line(self.maker_screen,'white',(i*self.xinc,0),(i*self.xinc,self.maker_screen_rect.h)) for i in range(1,int(self.maker_screen_rect.w/self.xinc))]        
        [pygame.draw.line(self.maker_screen,'white',(0,i*self.yinc),(self.screen_rect.w*self.xStretch,i*self.yinc))for i in range(1,res[1])]

        # Platforms
        [self.maker_screen.blit(self.platforms[i].image,(self.platforms[i].rect.x,self.platforms[i].rect.y)) for i in range (len(self.platforms))]
        # Enemies
        [self.maker_screen.blit(self.enemies[i].image,(self.enemies[i].rect.x,self.enemies[i].rect.y)) for i in range (len(self.enemies))]
        # Berries
        [self.maker_screen.blit(self.berries[i].image,(self.berries[i].rect.x,self.berries[i].rect.y)) for i in range (len(self.berries))]
        # Player
        self.maker_screen.blit(self.player.image,(self.player.rect.x,self.player.rect.y))

        if self.boss!=None:
            self.maker_screen.blit(self.boss.image,(self.boss.rect.x,self.boss.rect.y))

        # Blit to Main Screen
        r = pygame.Rect(self.lateral,0,self.screen_rect.w-self.display_cords[1],self.maker_screen_rect.h)
        self.screen.blit(self.maker_screen,self.display_cords,r)

    def showMenus(self):
        # Top Bar
        if self.topSel!='':
            if self.topSel=='platforms':
                ind = 1
            elif self.topSel=='berries':
                ind = 2
            elif self.topSel=='enemies':
                ind = 3
            else:
                ind = 4
            r = self.top_bar_btns[ind].rect.copy()
            r.w=r.w*1.1
            r.h=r.h*1.1
            r.center = (self.top_bar_btns[ind].rect.center)
            r.y=r.y-self.top_bar[1]/30
            pygame.draw.rect(self.screen,'yellow',r)
        [btn.show() for btn in self.top_bar_btns]
        # Side Bar
        if self.side_bar_btns!=[] and self.sideSel!=-1:
            r = self.side_bar_btns[self.sideSel].rect.copy()
            r.w=r.w*1.3
            r.h=r.h*1.3
            r.center = (self.side_bar_btns[self.sideSel].rect.center)
            pygame.draw.rect(self.screen,'yellow',r)
        [btn.show() for btn in self.side_bar_btns]

    def run(self):
        self.input()
        self.show()
    
    def save(self):
        # Platforms
        platform_message = "\n".join([" ".join(map(str,line)) for line in [data for data in [p.returnData() for p in self.platforms]]])
        platformFile = open(Path(r'Code/levels/makerLevel/platforms.txt'),'w')
        platformFile.write(platform_message)

        # Enemies
        enemy_message = "\n".join([" ".join(map(str,line)) for line in [data for data in [p.returnData() for p in self.enemies]]])
        enemyFile = open(Path(r'Code/levels/makerLevel/enemies.txt'),'w')
        enemyFile.write(enemy_message)

        # Berries
        berry_message = "\n".join([" ".join(map(str,line)) for line in [data for data in [p.returnData() for p in self.berries]]])
        berryFile = open(Path(r'Code/levels/makerLevel/berries.txt'),'w')
        berryFile.write(berry_message)

        # Bosses
        if self.boss == None:
            return
        boss_message = "\n".join([" ".join(map(str,self.boss.returnData()))])
        bossFile = open(Path(r'Code/levels/makerLevel/boss.txt'),'w')
        bossFile.write(boss_message)

        platformFile.close()
        berryFile.close()
        enemyFile.close()
        bossFile.close()
        importlib.reload(gameData)
        importlib.reload(runnables.map)
        importlib.reload(runnables.level)
