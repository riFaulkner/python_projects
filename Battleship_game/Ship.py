'''
Created on Jul 21, 2015

@author: Rick
'''
class GamePiece(object):
    def __init__(self, name, position, lives=1):
        self.name = name
        self.livesLeft = lives
        self.position = position
    
class Ship(GamePiece):
    postion = []
    
    def __init__(self, name, position, lives):
        super.__init__(name,position)
        self.initialLives = lives
    
    def hit(self):
        self.livesLeft -= 1
        
        if self.livesLeft == 0:
            return "You've sunk my %s" % (self.name)
        else:
            return "Thats a hit!!"
        
    def lives(self):
        return self.livesLeft