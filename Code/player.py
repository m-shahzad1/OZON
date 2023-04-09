import pygame
from levelObjects import LevelObject
from gameData import player_size,players,projectiles
from projectiles import Projectile 
from gameObjects import GameObject

class Player(LevelObject):
    def __init__(self, screen, rect,start_pos,playerType,attackUnlocked):
        # player animation pictures 
        self.walkRight_imgs = players[playerType]['sprite']['walkRight']
        self.walkLeft_imgs = players[playerType]['sprite']['walkLeft']
        self.lookRight_imgs = players[playerType]['sprite']['lookRight']
        self.lookLeft_imgs = players[playerType]['sprite']['lookLeft']
        self.jumpRight_imgs = players[playerType]['sprite']['jumpRight']
        self.jumpLeft_imgs = players[playerType]['sprite']['jumpLeft']


        #player movement     
        self.isJump = False
        self.left = False
        self.right = False
        self.lookLeft = False
        self.lookRight = False
        self.walkCount = 0

        # player stats
        self.top_speed = players[playerType]['vel']
        self.health = players[playerType]['health']
        self.prevHealth = self.health
        self.maxHealth = self.health
        self.maxJump = players[playerType]['maxJumpHeight']
        self.acc_const = 3

        #player physics     
        self.jumping = False
        self.jumpOrgin = 0
        self.jumpvelo = 60
        self.g = 13
        self.maxheighthit = False
        self.hitPlat = []

        super().__init__(screen,rect,start_pos[0],start_pos[1],start_pos[0]+player_size[0],start_pos[1]+player_size[1],self.lookRight_imgs[0])

        # attacks 
        self.attacks = [projectiles['normalBall']]
        if int(attackUnlocked) >= 1:
           self.attacks.append(projectiles['fireBall'])
        if int(attackUnlocked) >= 2:
           self.attacks.append(projectiles['iceBall'])
        
        self.attack_imgs=[]
        for a in self.attacks:
            self.attack_imgs.append(GameObject(screen,pygame.Rect(screen.get_rect().h/15,screen.get_rect().h/15,screen.get_rect().h/10,screen.get_rect().h/10),a['img']))
        
        self.attack_index = 0

        #Projectile Parameters 
        self.projectiles = []
        self.damage = 10
        ##Must PROGRAM ANGLE MECHANICS
        self.angle = 45
        self.velocity = 5

        #health 
        self.invinsibility = False    


    # gets input from user and checks sets values for player movement accordingly 
    def get_input(self,lateral):
        keys = pygame.key.get_pressed()

        if keys [pygame.K_SPACE]:
            if not self.isJump:
                self.jumpOrgin = self.rect.bottom
                self.jumping = True
                self.isJump = True
            self.jump()

        if keys [pygame.K_d]:
            self.setAcc((self.acc_const, self.acc[1]))
            self.left = False
            self.right = True
            self.lookLeft = False
            self.lookRight = True


        elif keys [pygame.K_a]:
            self.setAcc((-self.acc_const,self.acc[1]))
            self.left = True
            self.right = False
            self.lookLeft = True
            self.lookRight = False

        else:
            self.setAcc((0,self.acc[1]))
            self.left = False
            self.right = False

        if keys [pygame.K_1]:
            self.attack_index = 0

        elif keys [pygame.K_2] and len(self.attacks)>=1:
            self.attack_index = 1

        elif keys [pygame.K_3] and len(self.attacks)>=2:
            self.attack_index = 2
        

        ###SHOOTING
        left, middle, right = pygame.mouse.get_pressed()

        if left: 
            mouse_x,mouse_y = pygame.mouse.get_pos()
            mouse_x=mouse_x+lateral
            self.shoot(mouse_x,mouse_y)
        
    def character_animations(self):
        # cycles through walking animations
        if self.walkCount + 1 > 10:
            self.walkCount = 0

        img = self.lookRight_imgs[0]

        # selects image for type of animation
        if self.isJump and self.lookRight:
            img = self.jumpRight_imgs[0]
            self.walkCount = 0
        elif self.isJump and self.lookLeft:
            img = self.jumpLeft_imgs [0]
            self.walkCount = 0    
        elif self.left:  
            img = self.walkLeft_imgs[self.walkCount//2]
            self.walkCount += 1                          
        elif self.right:
            img = self.walkRight_imgs[self.walkCount//2]
            self.walkCount += 1
        elif self.lookRight:
            img = self.lookRight_imgs[0]
            self.walkCount = 0
        elif self.lookLeft:
            img = self.lookLeft_imgs[0]
            self.walkCount = 0
            
        # sets the selected image
        self.setImage(str(img))

# JUMP
    # jumps the player 
    def jump(self):
        if self.rect.bottom > self.jumpOrgin - self.maxJump and self.jumping == True:
            self.setVelo((self.velo[0],-self.jumpvelo))
        elif self.maxheighthit==False:
            self.setVelo((self.velo[0],-self.jumpvelo))
            self.maxheighthit = True
            self.jumping = False

    # checks if player is on ground to allow jump 
    def jump_return(self, platforms):
            p = self.collision_check(platforms)
            if p[0] =='top' and not p[1] in self.hitPlat:
                self.isJump = False
                self.maxheighthit = False
                self.hitPlat = [ ]
            #self.jump_hit(platforms)

    # checks if player jump hits the top (in the works)
    def jump_hit(self, platforms):
        p = self.collision_check(platforms)
        if p[0] =='bottom':
            self.hitPlat.append(p[1])
            self.maxheighthit = True
            self.jumping = False
        

# PROJECTILES
    # shoots projectiles
    def shoot(self,x,y):
        currentTime = pygame.time.get_ticks()
        if len(self.projectiles) == 0:
            self.projectiles.append(Projectile(self.screen,(self.rect.centerx,self.rect.centery),x,y, self.attacks[self.attack_index]))
            # previousProj = self.projectiles[numberOfProjectiles-1]
        else:
            numberOfProjectiles = len(self.projectiles)
            previousProj = self.projectiles[numberOfProjectiles-1]
            if (currentTime-previousProj.getTimeCreated()>1000):
                self.projectiles.append(Projectile(self.screen,(self.rect.centerx,self.rect.centery),x,y, self.attacks[self.attack_index]))

    # gets the projectile type
    def get_projectiletype(self):
        return self.attacks[self.attack_index]['type']
    
    # removes a projectile 
    def remove_shoot(self, p):
        self.projectiles.remove(p)

# PARAMETERS
    # applies gravity to player 
    def gravity(self):
        self.setAcc((self.acc[0],self.g))

    #applies friction to the player and platfrom
    def friction(self):
        if abs(self.velo[0]) > 0 and self.acc[0]==0:
            self.setVelo((self.velo[0]*0.80,self.velo[1]*0.80))

    # checks has fallen off the screen
    def falloff(self):
        if self.rect.bottom > self.screen.get_rect().bottom:
            self.health = 0
            # kill the player

    # checks if the player is at the edge of the screen
    def edge_Collide(self):
        if self.rect.left < self.screen.get_rect().left:
            self.rect.left = self.screen.get_rect().left
        elif self.rect.right > self.screen.get_rect().right:
            self.rect.right = self.screen.get_rect().right
            # kill the player

# HEALTH CHNAGES (enemy attck, berries, health bar)
    def enemny_attack(self, damage):
        #makes the player invisible for 1 second after damage 
        if self.invinsibility == False:
            self.invinsibilityTime = pygame.time.get_ticks()
            self.health -= damage
            self.invinsibility = True

        if (pygame.time.get_ticks()-self.invinsibilityTime) > 1000:
            self.invinsibility = False

    # gives player health if it colides with a berry 
    def give_health(self, type):
        if type == 'full' and self.maxHealth >= self.health + 20:
            self.health += 20

        if type == 'part' and self.maxHealth >= self.health + 10:
            self.health += 10

    def health_bar(self):
        r = pygame.Rect(self.rect.left,self.rect.top - 15,self.rect.w,10)
        pygame.draw.rect(self.screen, (169,169,169), r)
        r2 = pygame.Rect(self.rect.left,self.rect.top - 15,(self.health/self.maxHealth)*self.rect.w,10)
        pygame.draw.rect(self.screen, 'green', r2)

        if self.prevHealth > self.health:
            r3 = pygame.Rect(r2.right,self.rect.top - 15,((self.prevHealth-self.health)/self.maxHealth)*self.rect.w,10)
            pygame.draw.rect(self.screen, 'red', r3)
            self.prevHealth = self.health

    def update(self):
        # removes projectiles
        [p.update() for p in self.projectiles]

        for p in self.projectiles:
            if p.remove() == True:
                self.projectiles.remove(p)

        #applies friction
        self.friction()

        # checks if player goes off screen
        self.falloff()

        #applies player annimations 
        self.character_animations()

        #applies gravity 
        self.gravity()

        #checks if player hits an edge
        self.edge_Collide()

        #limits player velocity 
        if abs(self.velo[0])>self.top_speed:
            if self.velo[0]>0:
                self.setVelo((self.top_speed,self.velo[1]))
            else:
                self.setVelo((-self.top_speed,self.velo[1]))
        if self.velo[1]>40:
            self.setAcc((self.acc[0],0))
            self.setVelo((self.velo[0],40))


        super().update()
    
    def show(self):
        self.health_bar()
        [p.show() for p in self.projectiles]
        super().show()
