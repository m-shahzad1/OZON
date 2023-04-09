from gameData import berry_size
from levelObjects import LevelObject


class Berry(LevelObject):
    def __init__(self,screen,rect,data):
        self.data = data 
        self.type = data[2]
        super().__init__(screen,rect,int(data[0]),int(data[1]),int(data[0])+berry_size[0],int(data[1])+berry_size[1],data[3]) 

    def returnData(self):
        return self.data
        
        