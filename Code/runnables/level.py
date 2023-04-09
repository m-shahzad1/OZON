import pygame,math,importlib,time
import gameData
importlib.reload(gameData)

from gameData import levels,res,maker_sprites,players,map_unlock
from block import Platform
from player import Player
from berry import Berry
from enemy import Enemy
from boss import Boss
from gameObjects import GameObject
from pathlib import Path
#from backgroundMusic import Music


class Level:
    def __init__(self,screen,level,enterMap):

        importlib.reload(gameData)
        # level
        self.level = levels[level]
        self.currentLevel = level # This is the level number
        # screen
        self.screen = screen
        self.rect = screen.get_rect()

        # Display
        self.display = pygame.Surface((self.rect.w*self.level['stretch'],self.rect.h)).convert()
        self.display_rect = self.display.get_rect()
        self.display.fill('violet')
        self.display.set_colorkey('violet')

        # Scroller
        self.left_bound = self.rect.w/5
        self.right_bound = self.left_bound*4

        # Background
        backRect = self.rect.copy()
        backRect.w=backRect.w*1.4
        # self.background = GameObject(self.screen,backRect,maker_sprites['backgrounds']['night'])
        self.background = GameObject(self.screen,backRect,self.level['map'])

        self.setup()

        # map
        self.enterMap = enterMap

        # Music
        # self.playBackgroundMusic()


    def setup(self):
        # Scroller
        self.lateral = 0
        # this same logic will be used for enemies, bosses, coins, powerups, etc

        self.platforms = []
        self.berries = []
        self.boss = None
        self.enemies = []


        # Platforms
        if self.level['platforms']!=[['']]:
            self.platforms = [Platform(self.display,self.rect,p) for p in self.level['platforms']]

        # Berries
        if self.level['berries']!=[['']]:
            self.berries = [Berry(self.display,self.rect,b) for b in self.level['berries']]

        # Enemies
        if self.level['enemy']!=[['']]:
            self.enemies = [Enemy(self.display,self.rect,e) for e in self.level['enemy']]
        self.EnColOn = 0

        # Bosses
        if self.level['boss']!=['']:
            self.boss = Boss(self.display,self.rect,self.level['boss'])

        # Player
        playerType = players['selected']
        playerAttacks = players['attackUnlock']
        self.player = Player(self.display,self.rect,self.level['player'],playerType, playerAttacks)

        # Effficeny 
        self.plats = [r.rect for r in self.platforms]
        self.fill = True
        #self.ens = []
        self.stillEnsLeft = []
        self.stillEnsRight = []

    def input(self):
        # Runs player input function
        self.player.get_input(self.lateral)

        # Return to map (REMOVE LATER)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.enterMap()
            return

    def show(self):
        # BACKGROUND AND CAMERA
        cam = pygame.Rect((self.background.rect.w-self.rect.w)*((self.rect.w+self.lateral)/self.display_rect.w),0,self.rect.w,self.rect.h)
        self.screen.blit(self.background.image,(0,0),cam)

        # Overwriting background for level
        self.display.fill('violet')

        # Grid System
        # [pygame.draw.line(self.screen,'black',(i*self.rect.w/res[0],0),(i*self.rect.w/res[0],self.rect.h))for i in range(1,res[0])]
        # [pygame.draw.line(self.screen,'black',(0,i*self.rect.h/res[1]),(self.rect.w,i*self.rect.h/res[1]))for i in range(1,res[1])]

        # Platforms
        [p.show() for p in self.platforms]

        # Enemies 
        [e.show() for e in self.enemies]
        
        # Bosses
        if self.boss != None:
            self.boss.show()

        #Berries
        [b.show() for b in self.berries]

        #Player
        self.player.show()

        # Draw Level
        r = pygame.Rect(self.lateral,0,self.rect.w,self.rect.h)
        self.screen.blit(self.display,(0,0),r)

        r = pygame.Rect(self.rect.h/20,self.rect.h/20,self.rect.w/5,self.rect.h/8)
        pygame.draw.rect(self.screen, 'darkblue', r)
        
        i=0
        for icon in self.player.attack_imgs:
            if self.player.attack_index==i:
                r = icon.rect.copy()
                r.w=r.w*1.3
                r.h=r.h*1.3
                r.center = icon.rect.center
                pygame.draw.rect(self.screen, 'yellow',icon.rect.move(i*self.rect.h/10,0))
            self.screen.blit(icon.image,icon.rect.move(i*self.rect.h/10,0))
            i=i+1

        
    
    def update(self):
        self.player.update() 
        self.cam_update()
        [e.update() for e in self.enemies]
        [p.update() for p in self.platforms]
        self.boss.update()
        self.collide()
        #self.enemy_shoot()
        self.end_level()
        #self.boss_shoot()

    def cam_update(self):
        p = self.player.rect
        if p.left < self.lateral+self.left_bound and self.lateral>0 and self.player.velo[0]<0:
            self.lateral+=self.player.velo[0]
        elif p.right>self.lateral+self.right_bound and self.player.velo[0]>0 and self.lateral<self.display_rect.w-self.rect.w:
            self.lateral+=self.player.velo[0]
        if self.lateral <0:
            self.lateral=0
        elif self.lateral>self.display_rect.w-self.rect.w:
            self.lateral = self.display_rect.w-self.rect.w
               
    def collide(self):
        # PLAYER COLLISION 
        
        #sort moving and still enemies
        enemyColl = False
        bossColl = False

        target = self.player.rect.center
        
        # gets the distnace between the boss and player 
        if self.distance(self.boss.rect.center, target) < 700:
            bossColl = True
        else:
            bossColl = False

        if self.player.velo[0] > 0:
            for r in self.stillEnsRight:
                if target[0] > r.rect.center[0]:
                    r.direction('right')
                    self.stillEnsRight.remove(r)
                    self.stillEnsLeft.append(r)
        if self.player.velo[0] < 0:
            for r in self.stillEnsLeft:
                if target[0] < r.rect.center[0]:
                    r.direction('left')
                    self.stillEnsLeft.remove(r)
                    self.stillEnsRight.append(r)

        ens = []

        for r in self.enemies:
            
            # gets the distnace between the enemy and player 
            if self.distance(r.rect.center, target) < 300:
                enemyColl = True
            else:
                enemyColl = False

            # fills enemy list  and shoots 
            if r.enemyType == 'enemyStill':
                if enemyColl:
                    r.shoot(target)
                # fills list once enemy
                    ens.append(r.rect)
                if self.fill:
                    self.stillEnsRight.append(r)

            # ENEMY COLLISON with platforms, only runs until all the enemys hit the platform 
            if self.EnColOn < len(self.enemies):
                enmColide = r.rect.collidelist(self.plats)
                if enmColide >= 0:
                    self.EnColOn += 1
                    r.setAcc((0, 0))
                    r.setVelo((r.top_speed, 0))
                    if r.data[2] == 'enemyMove':
                        r.set_edge(self.plats[enmColide], self.plats)

            # enemy projectile collision
            for p in r.projectiles:
                if self.player.rect.colliderect(p):
                    self.player.enemny_attack(p.damage)
                    r.remove_shoot(p)

            # player projectile collision with enemy 
            for p in self.player.projectiles:
                if r.rect.colliderect(p):
                    r.player_attack(p.damage)
                    r.got_hit(self.player.get_projectiletype())
                    self.player.remove_shoot(p)
      
            # ENEMY AND PLAYER COLLISION if distanmce is less than 300
            if enemyColl:
                if r.rect.colliderect(self.player.rect):
                    self.player.enemny_attack(r.hitdamage)

            # check enemy health 
            if r.health <= 0:
                if r in self.stillEnsRight:
                    self.stillEnsRight.remove(r)
                elif r in self.stillEnsLeft:
                    self.stillEnsLeft.remove(r)
                self.enemies.remove(r)


        self.fill = False
            
        # checks playeer and berry collisons and gives player heath 
        for b in self.berries:
            if self.distance(b.rect.center, target) < 300:
                if b.rect.colliderect(self.player.rect):
                    self.player.give_health(b.type)
                    self.berries.remove(b)

        # boss protectile collision 
        for p in self.boss.projectiles:
            if self.player.rect.colliderect(p):
                self.player.enemny_attack(p.damage)
                self.boss.remove_shoot(p)

        for p in self.player.projectiles:
            if self.boss.rect.colliderect(p):
                self.boss.player_attack(p.damage)
                self.boss.got_hit(self.player.get_projectiletype())
                self.player.remove_shoot(p)

        # player and boss collide
        if bossColl:
            self.boss.shoot(target)
            if self.boss.rect.colliderect(self.player.rect):
                self.player.enemny_attack(self.boss.hitdamage)

        all = self.plats+ens

        # checks once player has landed form a jump
        self.player.jump_return(all) 

        if self.player.isJump:
            self.player.jump_hit(self.plats)

        # collides player with platforms and still enemies
        self.player.collision(all)

    # def playBackgroundMusic(self):
    #     if self.currentLevel<= 2:
    #         pygame.mixer.music.load(Path(r'Code/Assets/Music/m4.mp3'))
    #     if self.currentLevel< 6 and self.currentLevel > 2:
    #         pygame.mixer.music.load(Path(r'Code/Assets/Music/m1.mp3'))
    #     if self.currentLevel == 6 or self.currentLevel == 7:
    #         pygame.mixer.music.load(Path(r'Code/Assets/Music/m2.mp3'))
    #     pygame.mixer.music.set_volume(0.5)
    #     pygame.mixer.music.play(-1,fade_ms=3000)

        #m1 =   grimes 2
        #m2 = kana yaari
        #m3 =turkish
        #m4 = grimes 1

            

    # sends projectile to player depending on enemy type
    # def enemy_shoot(self):
    #     #ens = [r.rect for r in self.enemies]
    #     for r in self.enemies:
    #         if r.get_enemyType() == 'enemyStill':
    #                 # if distance is less than a certain radius then the enemy will shoot
    #             if self.distance(r.rect.center, self.player.rect.center) < 300:
    #                 r.shoot(self.player.rect.center)
                
    #         # chnaghes looking direction for still enemies
    #             r.direction(self.player.rect.center)

    # def boss_shoot(self):
    #     if self.distance(self.boss.rect.center, self.player.rect.center) < 700:
    #         self.boss.shoot(self.player.rect.center)
    #         self.bossColl = True
    #     else:
    #         self.bossColl = False

    #gets distance between enemy and player
    def distance(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    
    # kills player if health is less than 0 
    def end_level(self):
        if self.player.health <= 0:
            # REBOOT LEVEL
            self.setup()
        if self.boss.health <= 0:
            # Level Completed
            if self.currentLevel==len(levels)-1:
                # MINI LEVEL
                self.enterMap()
                return
            if int(map_unlock)<7:
                if self.currentLevel>=int(map_unlock):
                    a = [a for a in open(Path('Code/data/master.txt')).read().split(' ')]
                    msg = a[0]+" "+str(self.currentLevel+1)+" "+a[2]
                    f = open(Path(r'Code/data/master.txt'),'w')
                    f.write(msg)
                    f.close()
                    importlib.reload(gameData)
            self.enterMap()

    def run(self):
        self.input()
        self.show()
        self.update()
