import pygame,time,importlib
import gameData
importlib.reload(gameData)
from gameData import sequences
from gameObjects import GameObject

#TO-DO: ADD EVENTS.GET FUNCTIONALITY

class Seq():
    def __init__(self,screen,option,enterMap):

        # ENTER MAP FUNCTION
        self.enter_map = enterMap
        self.option = option
        self.screen = screen

        # METHOD THAT ASSIGNS THE IMAGES BASED OFF OPTION
        if option == 'start':
            self.sequence_imgs = [GameObject(screen,screen.get_rect(),img_loc) for img_loc in sequences[0]['imgs']]
        else:
            pygame.mixer.music.load('Code\Assets\Music\m3.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1,fade_ms=3000)
            self.sequence_imgs = [GameObject(screen,screen.get_rect(),img_loc) for img_loc in sequences[1]['imgs']]
        
        self.counter = 0

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

        if mpos[0] >= 700 and mpos[0] <= 980 and mpos[1] >= 530 and mpos[1] <= 580 and mpress[0] == True:#if you want user to do right click on mouse
            ##print(mpos[0],mpos[1])
            self.counter+=1
            #self.enter_map()
            time.sleep(0.5)
            
       
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.enter_map()
            
        if self.counter == len(self.sequence_imgs):
            self.enter_map()
            return
        self.sequence_imgs[self.counter].show()
     