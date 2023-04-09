import pygame,importlib
import gameData
importlib.reload(gameData)
from gameObjects import GameObject
from pathlib import Path

#TO-DO: ADD EVENTS.GET FUNCTIONALITY

class Menu():
    def __init__(self,screen,enterStartSequence):

        # ENTER MAP FUNCTION
        self.enter_start_sequence = enterStartSequence
        self.screen = screen

        # METHOD THAT ASSIGNS THE IMAGES BASED OFF OPTION

        self.background = GameObject(screen,screen.get_rect(),Path('Code/Assets/menu.png'))
    
        
        

        # #Populating the list of images for the starting sequence
        # for i in range(1, 10):
        #     filename = f"Code\Assets\startSequence{i}.png"
        #     image = pygame.image.load(filename)
        #     start_seqs.append(image)

        # #Populating the list of images for the ending sequence
        # for i in range (1,5):
        #     filename = f"Code\Assets\EndingSequence{i}.png"
        #     image = pygame.image.load(filename)
        #     end_seqs.append(image)

    def input(self):
        keys = pygame.key.get_pressed()

        mpos = pygame.mouse.get_pos()
        mpress = pygame.mouse.get_pressed()
        if mpress[0]==True:
            #print(mpos[0],mpos[1])
            pass

        screenWidth = self.screen.get_width()
        screenHeight = self.screen.get_height()
        howToBtn = pygame.Rect(screenWidth*(0.205),screenHeight*(205/600),screenWidth*(0.120),screenHeight*(45/600)) #Button to How to play
        startBtn = pygame.Rect(screenWidth*(0.205),screenHeight*(140/600),screenWidth*(0.120),screenHeight*(45/600)) #Button to Start Sequence
        startBtn2 = pygame.Rect(screenWidth*(0.805),screenHeight*(535/600),screenWidth*(0.120),screenHeight*(45/600)) #Button to Start Sequence
        #Top, left, width, hseight
        #205,210,120,40
        #850,535,120,40
        if howToBtn.collidepoint(pygame.mouse.get_pos()):
            if mpress[0]==True:
                self.background=  GameObject(self.screen,self.screen.get_rect(),Path('Code/Assets/howTo.png'))
        
        if startBtn.collidepoint(pygame.mouse.get_pos()):
            if mpress[0]==True:
                self.enter_start_sequence()

        if startBtn2.collidepoint(pygame.mouse.get_pos()):
            if mpress[0]==True:
                self.enter_start_sequence()

    def run(self):
        #Iterating between each of the starting sequences images
        # if self.option == 'start':
        #     for counter in range(0,9):
        #         screen.blit(start_seqs[counter],(0,0))
        #         pygame.display.update()
        #         time.sleep(1.00)
        # #Iterating between each of the ending sequence images
        # if self.option == 'end':
        #     for counter in range (0,4):
        #         screen.blit(end_seqs[counter],(0,0))
        #         pygame.display.update()
        #         time.sleep(1.00)

        self.input()
        self.show()

    def show(self):
        #if self.counter == len(self.sequence_imgs):
         ##  return
        #self.sequence_imgs[self.counter].show()
        self.background.show()