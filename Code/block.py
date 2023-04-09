from levelObjects import LevelObject

class Platform (LevelObject):
    def __init__(self,screen,rect,data):
        self.data = data
        super().__init__(screen,rect,int(data[0]),int(data[1]),int(data[2]),int(data[3]),data[5])

    # Maker (Data to print to txt file)    
    def returnData(self):
        return self.data
    
    def update(self):
        pass