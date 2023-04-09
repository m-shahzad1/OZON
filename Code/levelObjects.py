import pygame
from gameObjects import GameObject
from gameData import res
from pathlib import Path

class LevelObject(GameObject):
    def __init__(self,screen,rect,x1,y1,x2,y2,img_path):
        rect = rect
        self.x = rect.w*x1/res[0]
        self.y = rect.h*(res[1]-y1)/res[1]
        self.w = rect.w*((1+x2-x1)/res[0])
        self.h = rect.h*((1+y2-y1)/res[1])
        self.r = pygame.Rect(self.x,self.y,self.w,self.h)
        self.r.bottomleft = (self.x,self.y)
        super().__init__(screen,self.r,img_path)

    def collision(self, plats):
        # takes a list of rects to see if a collision happened and doesnt allow them to over lap 
        # r2 = col_rect.bottomleft
        # r2size = col_rect.size
        s = self.rect

        s.move_ip(-self.velo[0],-self.velo[1])

        # X axis collision
        s.move_ip(self.velo[0],0)
        for r in plats:
            if s.colliderect(r):
                #Right
                if self.velo[0] > 0:
                    if s.right > r.left:
                        s.right =  r.left
                #left
                elif self.velo[0] < 0:
                    if s.left<r.right:
                        s.left = r.right

        # Y axis collision
        s.move_ip(0,self.velo[1])
        for r in plats:
            if s.colliderect(r):
                #top
                if self.velo[1] > 0:
                    if s.bottom>r.top:
                        s.bottom = r.top
                #bottom
                elif self.velo[1] < 0:
                    if s.top<r.bottom:
                        s.top = r.bottom

        # Pull rects apart WONT WORK FOR MOVING PLATFORMS
        # while(self.rect.colliderect(r)):
        #     self.rect.move(-self.velo[0]*0.05,-self.velo[1]*0.05)
        # self.rect.move(self.velo[0],self.velo[1])       
                    

    def collision_check(self, plats):
    
        s = self.rect.copy()

        #s.move_ip(0,-self.velo[1])

        # Y axis collision
        s.move_ip(0,self.velo[1])
        for r in plats:
            if s.colliderect(r):
                #top
                if self.velo[1] > 0:
                    if s.bottom>r.top:
                        return ['top', r]
                # #bottom
                # el
                elif self.velo[1] < 0:
                    if s.top<r.bottom:
                        return ['bottom', r]
        return [False, False]               

    


